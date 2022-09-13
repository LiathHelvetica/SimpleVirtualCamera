POINT_CLASS_TAG = "point"


class Point:
	def __init__(self, x, y, z, id=None, store=None):
		self.id = id
		self.x = int(x)
		self.y = int(y)
		self.z = int(z)

		if store is not None:
			store.register(self, id)

	def to_vector(self):
		return [self.x, self.y, self.z, 1]

	def copy(self, entity_store):
		return Point(self.x, self.y, self.z, self.id, entity_store)

	def __repr__(self):
		id = self.id if self.id is not None else "p"
		return f"{id}: ({self.x}, {self.y}, {self.z})"
