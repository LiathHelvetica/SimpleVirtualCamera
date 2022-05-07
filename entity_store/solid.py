class Solid:
	def __init__(self, walls, id, store):
		self.id = id
		self.walls = {}

		for wall in walls:
			self.walls[wall.id] = wall

		store.register(self, id)
