import pyglet
from pyglet.gl import *
import cocos
from cocos.director import director
from cocos.actions import *
from cocos.particle_systems import Explosion
from cocos.menu import *
import math
import random
from collections import deque
import level
from mainmenu import paddedVerticalLayout

class GameModel(pyglet.event.EventDispatcher):
	def __init__(self):
		super(GameModel, self).__init__()

		# Get levels
		self.levels = level.get_levels()
		self.current_level = None
		self.num_wave = 0
		self.num_level = 0
		# Add the player
		self.player = Player()
		self.player.position = 400, 300
		# Node for player bullets
		self.player_bullets = cocos.batch.BatchNode()
		# Node for enemy bullets
		self.enemy_bullets = cocos.batch.BatchNode()
		# Node for particles
		self.particles = cocos.cocosnode.CocosNode()
		# Message box that will displayed in between waves and levels
		w, h = director.get_window_size()
		self.message = cocos.text.Label('nothing', color=(50, 50, 50, 255), font_name='Orbitron', font_size=40, anchor_x='center', anchor_y='center')
		self.message.position = w/2, h/2
		self.message.visible = False
		# Register player event listeners
		self.player.push_handlers(self)
		# Paused flag
		self.paused = False
		self.pause_menu = PauseMenu(self)

	def pause(self):
		if not self.paused:
			self.paused = True
			self.dispatch_event('on_pause')
			# Pause everything... what a mess... oh well no time for love
			self.player.pause_scheduler()
			self.player.pause()
			self.player_bullets.pause_scheduler()
			self.player_bullets.pause()
			for b in self.player_bullets.get_children():
				b.pause()
				b.pause_scheduler()
			self.enemy_bullets.pause_scheduler()
			self.enemy_bullets.pause()
			for b in self.enemy_bullets.get_children():
				b.pause()
				b.pause_scheduler()
			self.current_level.pause_scheduler()
			self.current_level.pause()
			self.particles.pause_scheduler()
			self.particles.pause()
			for p in self.particles.get_children():
				p.pause()
				p.pause_scheduler()

	def resume(self):
		if self.paused:
			self.paused = False
			self.dispatch_event('on_resume')
			self.player.resume_scheduler()
			self.player.resume()
			self.player_bullets.resume_scheduler()
			self.player_bullets.resume()
			for b in self.player_bullets.get_children():
				b.resume()
				b.resume_scheduler()
			self.enemy_bullets.resume_scheduler()
			self.enemy_bullets.resume()
			for b in self.enemy_bullets.get_children():
				b.resume()
				b.resume_scheduler()
			self.current_level.resume_scheduler()
			self.current_level.resume()
			self.particles.resume_scheduler()
			self.particles.resume()
			for p in self.particles.get_children():
				p.resume()
				p.resume_scheduler()

	def next_level(self):
		# No levels left? WE HAVE A WINRAR!
		if len(self.levels) == 0:
			import getvictory
			self.current_level.player.pause()
			pyglet.resource.media('yeah.wav').play()
			director.replace(getvictory.get_scene(self.player.score))
			return

		self.current_level = self.levels.popleft()
		self.dispatch_event('on_new_level')
		self.current_level.push_handlers(self)
		self.next_wave()
	
	def next_wave(self):
		self.current_level.next_wave()
		for e in self.current_level.current_wave.get_children():
			e.push_handlers(self)
	
	def on_level_wave_complete(self):
		# Show wave complete message
		self.num_wave += 1
		self.message.element.text = 'WAVE %d COMPLETE' % self.num_wave
		def show():
			self.message.visible = True
		def hide():
			self.message.visible = False
		delay = 1
		self.message.do(CallFunc(show) + Delay(delay) + CallFunc(hide))
		self.current_level.do(Delay(delay) + (CallFunc(self.next_wave) | CallFunc(self.player.invuln)))
	
	def on_level_complete(self):
		# Show level complete message
		self.num_level += 1
		self.num_wave = 0
		self.message.element.text = 'LEVEL %d COMPLETE' % self.num_level
		def show():
			self.message.visible = True
		def hide():
			self.message.visible = False
		delay = 1
		self.message.do(CallFunc(show) + Delay(delay) + CallFunc(hide))
		self.current_level.do(Delay(delay) + CallFunc(self.next_level))

	def on_lose_life(self, lives):
		# Make an explosion particle effect
		p = Explosion()
		p.position = self.player.position
		self.particles.add(p)
		# Reset the player to the center of the screen
		w, h = director.get_window_size()
		self.player.position = w/2, h/2
		# If the player is out of lives it's game over.
		if lives == 0:
			import getgameover
			self.current_level.player.pause()
			director.replace(getgameover.get_scene(self.player.score))

	def on_bad_transform(self, enemy):
		self.player.chain = 0
	
	def on_enemy_death(self, enemy):
		self.player.chain += 1
		max_transforms = enemy.num_vertices / 2
		# Points multiplier
		# Full points awarded for taking n/2 or less transformations to kill enemy
		# Points reduced with each additional hit
		multiplier = max_transforms / float(max(max_transforms, enemy.num_transforms))
		self.player.score += enemy.num_vertices * 10 * multiplier
		p = Explosion()
		p.position = enemy.position
		self.particles.add(p)

	def on_player_fire(self, bullet):
		self.player_bullets.add(bullet)

	def on_enemy_fire(self, bullet):
		self.enemy_bullets.add(bullet)

	def step(self, dt):
		"""Checks for collisions.
		"""
		if not self.paused:
			# Some inefficient naive collision detection
			for b in self.player_bullets.get_children():
				for e in self.current_level.current_wave.get_children():
					if b.get_rect().intersects(e.get_rect()):
						b.on_hit(e)
						self.player_bullets.remove(b)
						return
			if not self.player.no_clip:
				for e in self.current_level.current_wave.get_children():
					if self.player.get_rect().intersects(e.get_rect()):
						self.player.on_hit()
						return
				for b in self.enemy_bullets.get_children():
					if b.get_rect().intersects(self.player.get_rect()):
						b.on_hit(self.player)
						self.enemy_bullets.remove(b)
						return

class PauseMenu(Menu):
	"""The pause menu.
	"""
	def __init__(self, model):
		super(PauseMenu, self).__init__('PAUSED')
		self.model = model
		# Menu item font properties
		self.font_title['font_name'] = 'Orbitron'
		self.font_title['color'] = (0, 0, 0, 255)
		self.font_item['font_name'] = 'Orbitron'
		self.font_item['color'] = (0, 0, 0, 255)
		self.font_item_selected['font_name'] = 'Orbitron'
		self.font_item_selected['color'] = (50, 50, 50, 255)
		# Create the menu items
		items = []
		items.append(MenuItem('Resume', self.on_resume))
		items.append(MenuItem('Quit', self.on_quit))

		# Finalize the menu
		self.create_menu(items, layout_strategy=paddedVerticalLayout(10))
	
	def on_resume(self):
		self.model.resume()
	
	def on_quit(self):
		# Pop this scene off of the scene stack.
		self.model.current_level.player.pause()
		director.pop()

GameModel.register_event_type('on_new_level')
GameModel.register_event_type('on_pause')
GameModel.register_event_type('on_resume')

class RemoveBoundedMove(cocos.actions.move_actions.Move):
	"""Move the target but remove it from the parent when it reaches certain bounds.
	Modified from the cocos2d sources to fit the needed purpose.
	This action is used for bullets.
	"""
	def init(self, width, height):
		self.width, self.height = width, height

	def step(self, dt):
		super(RemoveBoundedMove, self).step(dt)
		x, y = self.target.position
		w, h = self.target.width, self.target.height
		# Out of bounds, remove the node from the parent
		if x > self.width + w/2 or x < 0 - w/2 or y > self.height + h/2 or y < 0 - h/2:
			self.target.parent.remove(self.target)

		self.target.position = (x, y)

class Bullet(cocos.sprite.Sprite):
	"""Provides the functionality to create differing bullet types by using event handlers.
	"""
	def __init__(self, image_file, dx=0, dy=500):
		"""dx and dy parameters set the bullet speed and vector.
		"""
		super(Bullet, self).__init__(image_file)
		self.velocity = dx, dy
		w, h = director.get_window_size()
		self.do(RemoveBoundedMove(w, h))
	
	def step(self, dt):
		self.x += self.dx * dt
		self.y += self.dy * dt

	def on_hit(self, entity):
		"""Hit event handler.
		Customize this to do what you want the bullet to do.
		"""
		pass

class RotateCWBullet(Bullet):
	"""Bullet that will rotate an enemy's kill vertex one 'step' clockwise.
	"""
	def __init__(self):
		super(RotateCWBullet, self).__init__('rotate_cw_bullet.png')
	
	def on_hit(self, entity):
		if entity.no_shield:
			entity.rotate_cw()

class RotateCCWBullet(Bullet):
	"""Bullet that will rotate an enemy's kill vertex one 'step' counter clockwise.
	"""
	def __init__(self):
		super(RotateCCWBullet, self).__init__('rotate_ccw_bullet.png')
	
	def on_hit(self, entity):
		if entity.no_shield:
			entity.rotate_ccw()
		
class FlipLeftBullet(Bullet):
	"""Bullet that will flip an enemy by it's left axis of symmetry.
	"""
	def __init__(self):
		super(FlipLeftBullet, self).__init__('flip_left_bullet.png')
	
	def on_hit(self, entity):
		if entity.no_shield:
			entity.flip_l()

class FlipRightBullet(Bullet):
	"""Bullet that will flip an enemy by it's right axis of symmetry.
	"""
	def __init__(self):
		super(FlipRightBullet, self).__init__('flip_right_bullet.png')
	
	def on_hit(self, entity):
		if entity.no_shield:
			entity.flip_r()

class KillBullet(Bullet):
	"""Bullet that will kill an enemy that has its kill vertex exposed.
	"""
	def __init__(self):
		super(KillBullet, self).__init__('bullet.png')
	
	def on_hit(self, entity):
		if entity.kill_vertex == 0:
			entity.kill()

class EnemyBullet(Bullet):
	"""Enemies fire these. Go figure.
	"""
	def __init__(self, dx=0, dy=-300):
		super(EnemyBullet, self).__init__('enemy_bullet.png', dx, dy)
	
	def on_hit(self, entity):
		# Player loses a life
		entity.lose_life()

class Player(cocos.sprite.Sprite):
	""" Our courageous hero!
	"""
	# Fuck yeah bit masks!
	MOVE_LEFT = 1
	MOVE_RIGHT = 2
	MOVE_UP = 4
	MOVE_DOWN = 8

	def __init__(self):
		cocos.sprite.Sprite.__init__(self, 'ship.png')
		self.move_mask = 0
		self.speed = 500
		w, h = director.get_window_size()
		self.do(cocos.actions.move_actions.BoundedMove(w, h))
		self.velocity = 0, 0
		self.no_clip = False
		self._lives = 9
		self._score = 0
		self._chain = 0
		self.hit_sound = pyglet.resource.media('PlayerDeath.mp3', streaming=False)
		self.fire_sound = pyglet.resource.media('QuickLaser.mp3', streaming=False)
		self.life_sound = pyglet.resource.media('yeah.wav', streaming=False)
	
	def _get_chain(self):
		return self._chain
	def _set_chain(self, chain):
		self._chain = chain
		if self._chain == 9:
			self.lives += 1
			self._chain = 0
			self.life_sound.play()
		self.dispatch_event('on_chain_change', self._chain)
	chain = property(_get_chain, lambda self,chain: self._set_chain(chain))

	def _get_lives(self):
		return self._lives
	def _set_lives(self, lives):
		self._lives= lives
		self.dispatch_event('on_lives_change', self._lives)
	lives = property(_get_lives, lambda self,lives: self._set_lives(lives))

	def _get_score(self):
		return self._score
	def _set_score(self, score):
		self._score = score
		self.dispatch_event('on_score_change', self._score)
	score = property(_get_score, lambda self,score: self._set_score(score))

	def get_rect(self):
		rect = super(Player, self).get_rect()
		rect.width -= 20
		rect.height -= 20
		rect.center = self.x, self.y
		return rect

	def move(self, direction):
		self.move_mask |= direction
		self.update_velocity()
	
	def stop_move(self, direction):
		self.move_mask &= ~direction
		self.update_velocity()
	
	def fire(self, bullet):
		# The player cannot fire when no_clip is on
		if not self.no_clip:
			bullet.position = self.position
			self.dispatch_event('on_player_fire', bullet)
			self.fire_sound.play()
	
	def update_velocity(self):
		dx = 0
		dy = 0

		if self.move_mask & self.MOVE_LEFT:
			dx = -self.speed
		if self.move_mask & self.MOVE_RIGHT:
			dx = self.speed
		if self.move_mask & self.MOVE_UP:
			dy = self.speed
		if self.move_mask & self.MOVE_DOWN:
			dy = -self.speed

		self.velocity = (dx, dy)
	
	def lose_life(self):
		self.invuln()
		self.lives -= 1
		self.chain = 0
		self.dispatch_event('on_lose_life', self.lives)
		self.hit_sound.play()
	
	def invuln(self):
		def func():
			self.no_clip = False
		self.no_clip = True
		self.do(cocos.actions.Blink(20, 1.5) + cocos.actions.CallFunc(func))
	
	def on_hit(self):
		self.lose_life()

Player.register_event_type('on_lose_life')
Player.register_event_type('on_chain_change')
Player.register_event_type('on_lives_change')
Player.register_event_type('on_score_change')
Player.register_event_type('on_player_fire')

class EnemyWeapon(object):
	"""Controls the pattern and rate with which the enemy fires bullets
	"""
	def __init__(self, enemy, action):
		self.enemy = enemy
		self.enemy.do(Repeat(action))
	
	def fire(self):
		pass

class BasicEnemyWeapon(EnemyWeapon):
	"""Fires bullets straight down
	"""
	def __init__(self, enemy, num_bullets, interval, intermission):
		super(BasicEnemyWeapon, self).__init__(enemy, Delay(intermission) + (CallFunc(self.fire) + Delay(interval)) * num_bullets)
	
	def fire(self):
		bullet = EnemyBullet()
		bullet.position = self.enemy.position
		self.enemy.dispatch_event('on_enemy_fire', bullet)

class FanEnemyWeapon(EnemyWeapon):
	"""Fires 3 streams of bullets straight down, and at a 45 degree to the left and right of the enemy's center x coordinate.
	"""
	def __init__(self, enemy, shoot_time, interval, intermission):
		self.speed = 300
		action = Delay(intermission) + (CallFunc(self.fire) + Delay(interval)) * int(shoot_time / interval)
		super(FanEnemyWeapon, self).__init__(enemy, action)
	
	def fire(self):
		bullet = EnemyBullet(dy=-self.speed)
		bullet.position = self.enemy.position
		self.enemy.dispatch_event('on_enemy_fire', bullet)
		bullet = EnemyBullet(self.speed, -self.speed)
		bullet.position = self.enemy.position
		self.enemy.dispatch_event('on_enemy_fire', bullet)
		bullet = EnemyBullet(-self.speed, -self.speed)
		bullet.position = self.enemy.position
		self.enemy.dispatch_event('on_enemy_fire', bullet)

class SweepEnemyWeapon(EnemyWeapon):
	"""Sprays bullets from side to side in a sweeping motion
	"""
	def __init__(self, enemy, sweep_time, shot_interval, intermission):
		self.speed = 300
		self.direction = 0
		action = Delay(intermission) + (CallFunc(self.fire) + Delay(shot_interval)) * int(sweep_time / shot_interval)
		super(SweepEnemyWeapon, self).__init__(enemy, action)
		self.sweep_time = sweep_time
		self.shot_interval = shot_interval
		self.intermission = intermission
	
	def fire(self):
		angle = self.direction*-math.pi
		self.direction += 0.1
		x = math.cos(angle) * self.speed
		bullet = EnemyBullet(dx=x, dy=-self.speed)
		bullet.position = self.enemy.position
		self.enemy.dispatch_event('on_enemy_fire', bullet)
	
class EnemyPolygon(cocos.cocosnode.CocosNode, pyglet.event.EventDispatcher):
	"""Our polygonal adversary.
	"""

	# Transformation constants for tracking last transformation applied
	ROTATE_CW = 1	
	ROTATE_CCW = 2
	FLIP_L = 3
	FLIP_R = 4

	def __init__(self, num_vertices, kill_vertex, radius=35, image_file='enemy1_ship.png', death_sound='MinionDeath.mp3'):
		#super(EnemyPolygon, self).__init__()
		cocos.cocosnode.CocosNode.__init__(self)
		pyglet.event.EventDispatcher.__init__(self)
		self.num_vertices = num_vertices
		# Maximum number of transforms to expose a kill vertex in the worst case is floor(n / 2)
		# We're dealing with ints so no need to floor the value
		self.max_hits = self.num_vertices / 2
		# Radius of shield
		self.radius = radius
		# Sprites that give a visual cue as to whether the kill vertex is exposed or not.
		self.no = cocos.sprite.Sprite('no.png')
		self.yes = cocos.sprite.Sprite('yes.png')
		# Enemy sprite
		# TODO: This will be customized on a per-enemy basis
		self.sprite = cocos.sprite.Sprite(image_file)
		self.add(self.sprite)
		# Assign the kill vertex to a non-downward vertex. The polygon's
		# downward vertex is zero, and the rest are numbered
		# incrementally counter-clockwise from the downward vertex.
		self.kill_vertex = kill_vertex
		self.update_sprites()
		# weapon
		self.weapon = None
		# Last transformation applied to this enemy
		self.last_transform = 0
		# Enemy shield - activated when player mistransforms
		self.no_shield = True
		# Counts the amount of transformation bullets that have hit.
		self.num_transforms = 0
		# Opacity
		self._opacity = 255
		# Sounds
		self.death_sound = pyglet.resource.media(death_sound, streaming=False)
		self.bad_sound = pyglet.resource.media('BadTransform.mp3', streaming=False)
		self.transform_sound = pyglet.resource.media('Bloop.mp3', streaming=False)
	
	def _get_opacity(self):
		return self._opacity
	def _set_opacity(self, opacity):
		self._opacity = opacity
		self.sprite.opacity = opacity
		self.no.opacity = opacity
		self.yes.opacity = opacity
	opacity = property(_get_opacity, lambda self, opacity: self._set_opacity(opacity))
	
	def get_rect(self):
		rect = self.sprite.get_rect()
		rect.width -= 10
		rect.height -= 10
		rect.center = self.position
		return rect
	
	def update_sprites(self):
		"""Sets the correct sprites based upon the kill vertex.
		"""
		if self.kill_vertex == 0:
			# This is a bit of a hack... it's just not pretty. It works, though.
			# Catch element not found exceptions
			try:
				self.remove(self.no)
			except:
				pass
			self.add(self.yes)
			angle = 2 * math.pi * self.kill_vertex / self.num_vertices - math.pi / 2
			self.yes.position = self.radius * math.cos(angle), self.radius * math.sin(angle)
		else:
			try:
				self.remove(self.yes)
			except:
				pass
			self.add(self.no)
			angle = 2 * math.pi * self.kill_vertex / self.num_vertices - math.pi / 2
			self.no.position = self.radius * math.cos(angle), self.radius * math.sin(angle)

	# Rotate clockwise
	def rotate_cw(self):
		self.num_transforms += 1
		if self.last_transform != self.ROTATE_CW:
			self.kill_vertex = (self.kill_vertex - 1) % self.num_vertices
			self.update_sprites()
			self.last_transform = self.ROTATE_CW
			self.transform_sound.play()
		else:
			self.bad_transform()

	# Rotate counter-clockwise
	def rotate_ccw(self):
		self.num_transforms += 1
		if self.last_transform != self.ROTATE_CCW:
			self.kill_vertex = (self.kill_vertex + 1) % self.num_vertices
			self.update_sprites()
			self.last_transform = self.ROTATE_CCW
			self.transform_sound.play()
		else:
			self.bad_transform()

	# Flip about line of symmetry passing through the side directly
	# to the left of the downward vertex
	def flip_l(self):
		self.num_transforms += 1
		if self.last_transform != self.FLIP_L:
			self.kill_vertex = (-self.kill_vertex - 1) % self.num_vertices
			self.update_sprites()
			self.last_transform = self.FLIP_L
			self.transform_sound.play()
		else:
			self.bad_transform()

	# Flip about line of symmetry passing through the side directly
	# to the right of the downward vertex
	def flip_r(self):
		self.num_transforms += 1
		if self.last_transform != self.FLIP_R:
			self.kill_vertex = (-self.kill_vertex + 1) % self.num_vertices
			self.update_sprites()
			self.last_transform = self.FLIP_R
			self.transform_sound.play()
		else:
			self.bad_transform()

	def bad_transform(self):
		def shield_up():
			self.no_shield = False
		def shield_down():
			self.no_shield = True
		self.do(cocos.actions.CallFunc(shield_up) + Delay(3) + cocos.actions.CallFunc(shield_down))
		self.dispatch_event('on_bad_transform', self)
		self.bad_sound.play()

	# Manage the death of the enemy polygon
	def kill(self):
		self.dispatch_event('on_enemy_death', self)
		self.death_sound.play()

	def draw(self):
		glPushMatrix()
		self.transform()
		# Draw polygon
		if not self.no_shield:
			glColor4f(0.0, 0.0, 1.0, self.opacity / 255.0)
		elif self.kill_vertex != 0:
			glColor4f(1.0, 0.0, 0.0, self.opacity / 255.0) # red color
		else:
			glColor4f(0.0, 1.0, 0.0, self.opacity / 255.0)
		glLineWidth(3)
		glEnable(GL_LINE_SMOOTH)
		# Construct polygon by its vertices, starting with the
		# downward vertex and working counter-clockwise
		# TODO: Put this stuff in a vertex buffer
		glBegin(GL_LINE_LOOP)
		for i in range(self.num_vertices):
			angle = 2 * math.pi * i / self.num_vertices - math.pi / 2
			glVertex2f(self.radius * math.cos(angle), self.radius * math.sin(angle))
		glEnd()
		glPopMatrix()
	
EnemyPolygon.register_event_type('on_enemy_fire')
EnemyPolygon.register_event_type('on_enemy_death')
EnemyPolygon.register_event_type('on_bad_transform')

class Nonagon(EnemyPolygon):
	"""The big kahuna. The rumble from down under. The brother from another mother. The one, the only: NONAGON!
	"""
	def __init__(self):
		super(Nonagon, self).__init__(9, 5, radius=80, image_file='nonagon_ship.png', death_sound='NonagonDeath.mp3')
	
	def on_enter(self):
		super(Nonagon, self).on_enter()
		cackle = pyglet.resource.media('WehHehHeh.mp3', streaming=False)
		cackle.play()
