EDGE_CLASS_TAG = "edge"


class Edge:
	def __init__(self, p1_id, p2_id, id):
		from entity_store import ENTITY_STORE

		self.id = id
		self.p1_id = p1_id
		self.p2_id = p2_id

		ENTITY_STORE.register(self, id)

	def get_point_pair(self, entity_store):
		return (
			entity_store.points[self.p1_id],
			entity_store.points[self.p2_id]
		)
