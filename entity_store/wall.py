from entity_store.edge import EDGE_CLASS_TAG

WALL_CLASS_TAG = "wall"


class Wall:
	def __init__(self, edges_ids, id, entity_id, store):
		from entity_reader import to_id

		self.id = id
		self.edges_ids = list(map(
			lambda edge_id: store.edges[to_id(entity_id, edge_id, EDGE_CLASS_TAG)],
			edges_ids
		))

		store.register(self, id)
