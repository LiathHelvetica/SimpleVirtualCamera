POINT_CLASS_TAG = "point"


class Point:
	def __init__(self, x, y, z, id):
		from entity_store import ENTITY_STORE

		self.id = id
		self.x = x
		self.y = y
		self.z = z

		ENTITY_STORE.register(self, id)

	def to_vector(self):
		return [self.x, self.y, self.z, 1]
