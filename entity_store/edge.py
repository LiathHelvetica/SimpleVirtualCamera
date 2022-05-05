EDGE_CLASS_TAG = "edge"


class Edge:
	def __init__(self, p1_id, p2_id, id):
		from entity_store import ENTITY_STORE

		self.id = id
		self.p1 = ENTITY_STORE.points[p1_id]
		self.p2 = ENTITY_STORE.points[p2_id]

		ENTITY_STORE.register(self, id)
