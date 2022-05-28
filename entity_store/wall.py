from entity_store.edge import EDGE_CLASS_TAG
from graphics_helpers.colour_map import map_to_edge_colour

WALL_CLASS_TAG = "wall"


class Wall:
	def __init__(self, edges_ids, id, entity_id, colour, store):
		from entity_reader import to_id

		self.id = id
		self.colour = colour
		self.edges_ids = set()
		for edge_id in edges_ids:
			edge_id_norm = to_id(entity_id, edge_id, EDGE_CLASS_TAG)
			self.edges_ids.add(edge_id_norm)
			store.edges[edge_id_norm].register_wall(id)

		store.register(self, id)

	def get_colour(self):
		return map_to_edge_colour(self.colour)
