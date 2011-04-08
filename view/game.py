import cocos

class GameView(cocos.layer.ColorLayer):
	def __init__(self, model):
		super(GameView, self).__init__(255, 255, 255, 255)
		self.model = model
		pad = 10
		w, h = cocos.director.director.get_window_size()
		self.lives = cocos.text.Label('Lives: %d' % self.model.player.lives, width=w-pad*2, color=(50, 50, 50, 255), font_name='Orbitron', font_size=20, anchor_x='left', anchor_y='center')
		self.lives.position = w/2, pad
		self.score = cocos.text.Label('Score: 0', width=w-pad*2, color=(50, 50, 50, 255), font_name='Orbitron', font_size=20, anchor_x='right', anchor_y='center')
		self.score.position =  pad, pad

		self.add(self.lives)
		self.add(self.score)
		self.add(self.model.player)
		self.add(self.model.player_bullets)
		self.add(self.model.enemy_bullets)
		self.add(self.model.level)
