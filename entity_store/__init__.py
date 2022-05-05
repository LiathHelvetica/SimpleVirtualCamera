from entity_store.edge import Edge
from entity_store.point import Point
from entity_store.solid import Solid
from entity_store.wall import Wall


class EntityStore:
	def __init__(self):
		self.points = {}
		self.edges = {}
		self.walls = {}
		self.solids = {}

		self.class_to_store_map = {
			Point.__name__: self.points,
			Edge.__name__: self.edges,
			Wall.__name__: self.walls,
			Solid.__name__: self.solids
		}

	def register(self, entity, id):
		self.class_to_store_map[type(entity).__name__][id] = entity

	def get_entity(self, class_ref, id):
		return self.class_to_store_map[class_ref.__name__][id]


ENTITY_STORE = EntityStore()
