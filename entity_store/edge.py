from graphics_helpers.colour_map import map_to_edge_colour

EDGE_CLASS_TAG = "edge"


class Edge:
	def __init__(self, p1_id, p2_id, id, colour, store):
		self.id = id
		self.p1_id = p1_id
		self.p2_id = p2_id
		self.colour = colour

		store.register(self, id)

	def get_point_pair(self, entity_store):
		return (
			entity_store.points[self.p1_id],
			entity_store.points[self.p2_id]
		)

	def get_colour(self):
		return map_to_edge_colour(self.colour)
