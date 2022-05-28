from graphics_helpers.colour_map import map_to_edge_colour

EDGE_CLASS_TAG = "edge"


class Edge:
	def __init__(self, p1_id, p2_id, id, colour, store):
		self.id = id
		self.p1_id = p1_id
		self.p2_id = p2_id
		self.colour = colour
		self.walls = set()

		store.register(self, id)

	def get_point_pair(self, entity_store):
		return (
			entity_store.points[self.p1_id],
			entity_store.points[self.p2_id]
		)

	def get_higher_vertex(self, entity_store):
		v1, v2 = self.get_point_pair(entity_store)
		return v1 if v1.y > v2.y else v2

	def get_y_ordered_vertices(self, entity_store):
		v1, v2 = self.get_point_pair(entity_store)
		return (v1, v2) if v1.y > v2.y else (v2, v1)

	def get_colour(self):
		return map_to_edge_colour(self.colour)

	def register_wall(self, wall_id):
		self.walls.add(wall_id)

	def __repr__(self):
		return f"[{self.p1_id} {self.p2_id}]"
