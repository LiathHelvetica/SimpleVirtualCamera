from properties import ASSETS_FILES
from properties import POINTS_KEY, EDGES_KEY, WALLS_KEY, ENTITIES_KEY
from properties import X_KEY, Y_KEY, Z_KEY
from entity_store.point import POINT_CLASS_TAG, Point
from entity_store.edge import EDGE_CLASS_TAG, Edge
from entity_store.wall import WALL_CLASS_TAG, Wall
from entity_store.solid import Solid
import json


def read_assets():
	for assets_file in ASSETS_FILES:
		with open(assets_file, "r") as file:
			assets = json.load(file)
			for entity_id, entity in assets[ENTITIES_KEY].items():
				for point_id, point in entity[POINTS_KEY].items():
					Point(point[X_KEY], point[Y_KEY], point[Z_KEY], to_id(entity_id, point_id, POINT_CLASS_TAG))

				for edge_id, edge in entity[EDGES_KEY].items():
					Edge(
						to_id(entity_id, edge[0], POINT_CLASS_TAG),
						to_id(entity_id, edge[1], POINT_CLASS_TAG),
						to_id(entity_id, edge_id, EDGE_CLASS_TAG)
					)

				walls_asset = entity[WALLS_KEY]
				walls = [None] * len(walls_asset)
				for wall_id, wall in enumerate(walls_asset):
					walls[wall_id] = Wall(wall, to_id(entity_id, wall_id, WALL_CLASS_TAG), entity_id)

				Solid(walls, entity_id)


def to_id(entity_id, sub_entity_id, sub_entity_class_tag):
	return f"{entity_id}-{sub_entity_class_tag}-{sub_entity_id}"
