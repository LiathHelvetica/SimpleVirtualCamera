class Solid:
	def __init__(self, walls, id):
		from entity_store import ENTITY_STORE

		self.id = id
		self.walls = {}

		for wall in walls:
			self.walls[wall.id] = wall

		ENTITY_STORE.register(self, id)
