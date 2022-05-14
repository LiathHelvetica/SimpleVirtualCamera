from entity_store.edge import Edge
from entity_store.point import Point
from entity_store.solid import Solid
from entity_store.wall import Wall


class EntityStore:
	def __init__(self, points=None, edges=None, walls=None, solids=None):
		self.points = {} if points is None else points
		self.edges = {} if edges is None else edges
		self.walls = {} if walls is None else walls
		self.solids = {} if solids is None else solids

		self.class_to_store_map = {
			Point.__name__: self.points,
			Edge.__name__: self.edges,
			Wall.__name__: self.walls,
			Solid.__name__: self.solids
		}

	def register(self, entity, id):
		self.class_to_store_map[type(entity).__name__][id] = entity

	def copy(self):
		entity_store = EntityStore(None, self.edges, self.walls, self.solids)
		entity_store.points = {point_id: pt.copy(entity_store) for point_id, pt in self.points.items()}
		return entity_store


ENTITY_STORE = EntityStore()
