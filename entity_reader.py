from properties import ASSETS_FILES
from properties import POINTS_KEY, EDGES_KEY, WALLS_KEY, ENTITIES_KEY, EDGE_DATA_KEY, EDGE_COLOUR_KEY
from properties import X_KEY, Y_KEY, Z_KEY
from entity_store.point import POINT_CLASS_TAG, Point
from entity_store.edge import EDGE_CLASS_TAG, Edge
from entity_store.wall import WALL_CLASS_TAG, Wall
from entity_store.solid import Solid
from entity_store import ENTITY_STORE
from graphics_helpers.colour_map import DEFAULT_COLOUR
import json


def read_assets():
	for assets_file in ASSETS_FILES:
		with open(assets_file, "r") as file:
			assets = json.load(file)
			for entity_id, entity in assets[ENTITIES_KEY].items():
				for point_id, point in entity[POINTS_KEY].items():
					Point(point[X_KEY], point[Y_KEY], point[Z_KEY], to_id(entity_id, point_id, POINT_CLASS_TAG), ENTITY_STORE)

				for edge_id, edge in entity[EDGES_KEY].items():
					edge_data = edge[EDGE_DATA_KEY]
					Edge(
						to_id(entity_id, edge_data[0], POINT_CLASS_TAG),
						to_id(entity_id, edge_data[1], POINT_CLASS_TAG),
						to_id(entity_id, edge_id, EDGE_CLASS_TAG),
						edge[EDGE_COLOUR_KEY] if EDGE_COLOUR_KEY in edge else DEFAULT_COLOUR,
						ENTITY_STORE
					)

				walls_asset = entity[WALLS_KEY]
				walls = [None] * len(walls_asset)
				for wall_id, wall in enumerate(walls_asset):
					walls[wall_id] = Wall(wall, to_id(entity_id, wall_id, WALL_CLASS_TAG), entity_id, ENTITY_STORE)

				Solid(walls, entity_id, ENTITY_STORE)


def to_id(entity_id, sub_entity_id, sub_entity_class_tag):
	return f"{entity_id}-{sub_entity_class_tag}-{sub_entity_id}"
