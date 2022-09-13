from entity_store.edge import EDGE_CLASS_TAG

WALL_CLASS_TAG = "wall"


class Wall:
	def __init__(self, edges_ids, id, entity_id, colour, edge_colour, store):
		from entity_reader import to_id

		self.id = id
		self.colour = colour
		self.edge_colour = edge_colour
		self.edges_ids = list(map(
			lambda edge_id: to_id(entity_id, edge_id, EDGE_CLASS_TAG),
			edges_ids
		))

		store.register(self, id)

	def get_vertices(self, entity_store):
		vertices_ids = set()
		for edge_id in self.edges_ids:
			edge = entity_store.edges[edge_id]
			vertices_ids.add(edge.p1_id)
			vertices_ids.add(edge.p2_id)
		return vertices_ids
