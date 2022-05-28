POINT_CLASS_TAG = "point"


class Point:
	def __init__(self, x, y, z, id, store):
		self.id = id
		self.x = int(x)
		self.y = int(y)
		self.z = int(z)

		store.register(self, id)

	def to_vector(self):
		return [self.x, self.y, self.z, 1]

	def copy(self, entity_store):
		return Point(self.x, self.y, self.z, self.id, entity_store)

	def __repr__(self):
		return f"({self.x}, {self.y}, {self.z})"
