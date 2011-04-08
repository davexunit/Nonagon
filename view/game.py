import cocos

class GameView(cocos.layer.ColorLayer):
	def __init__(self, model):
		super(GameView, self).__init__(255, 255, 255, 255)
		self.model = model
		pad = 10
		w, h = cocos.director.director.get_window_size()
		self.lives = cocos.text.Label('Lives: %d' % self.model.player.lives, width=w-pad*2, color=(50, 50, 50, 255), font_name='Orbitron', font_size=20, anchor_x='left', anchor_y='center')
		self.lives.anchor_x = 0
		self.lives.anchor_y = 0
		self.lives.position = pad, pad
		self.score = cocos.text.Label('Score: 0', width=w-pad*2, color=(50, 50, 50, 255), font_name='Orbitron', font_size=20, anchor_x='right', anchor_y='center')
		self.score.anchor_x = self.score.element.width
		self.score.anchor_y = 0
		self.score.position =  w - pad, pad
		self.chain = cocos.text.Label('Chain: 0', width=w-pad*2, color=(50, 50, 50, 255), font_name='Orbitron', font_size=20, anchor_x='center', anchor_y='center')
		self.chain.position = w/2, pad

		self.model.player.push_handlers(self)

		self.add(self.model.player)
		self.add(self.model.player_bullets)
		self.add(self.model.enemy_bullets)
		self.add(self.model.level)
		self.add(self.lives, z=1)
		self.add(self.score, z=1)
		self.add(self.chain, z=1)
	
	def on_chain_change(self, chain):
		self.chain.element.text = 'Chain: %d' % chain
	
	def on_lives_change(self, lives):
		self.lives.element.text = 'Lives: %d' % lives
	
	def on_score_change(self, score):
		self.score.element.text = 'Score: %d' % score
