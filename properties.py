from math import pi
from pyglet.window.key import UP, DOWN

PROJECT_NAME = "Simple Virtual Camera"

ASSETS_PATH_FORMAT = "assets/{0}"
FIGURE_FILES = ["figure2.json"]
ASSETS_FILES = list(map(
	lambda file_name: ASSETS_PATH_FORMAT.format(file_name),
	FIGURE_FILES
))

RESIZABLE = True

ENTITIES_KEY = "entities"
POINTS_KEY = "points"
EDGES_KEY = "edges"
WALLS_KEY = "walls"
EDGE_DATA_KEY = "data"
EDGE_COLOUR_KEY = "colour"
WALL_COLOUR_KEY = "colour"
WALL_DATA_KEY = "wall"

X_KEY = "x"
Y_KEY = "y"
Z_KEY = "z"

WINDOW_X_SIZE = 700
WINDOW_Y_SIZE = 500

SHIFT_OF_OBSERVER = 600

SHIFT_QUANTUM = 10
ROTATION_QUANTUM = pi / 30
ZOOM_QUANTUM = 1.1

TINY_NUMBER = 0.00000000000000001

DEFAULT_COLOUR = "white"
YELLOW_KEY = "yellow"

COLOUR_MAP = {
	"green": (0, 255, 0),
	"l-green": (170, 255, 170),
	"red": (255, 0, 0),
	"l-red": (255, 170, 170),
	"blue": (0, 0, 255),
	"l-blue": (170, 170, 255),
	"magenta": (255, 0, 255),
	"cyan": (0, 255, 255),
	"orange": (255, 165, 0),
	YELLOW_KEY: (255, 255, 0),
	DEFAULT_COLOUR: (255, 255, 255),
	"black": (0, 0, 0)
}

ZOOM_UP_KEY = UP
ZOOM_DOWN_KEY = DOWN

WITH_SURFACE_REMOVAL = False
DEBUG_INTERSECTIONS = True
DEBUG_COLOUR_KEY = YELLOW_KEY
DEBUG_COLOUR = COLOUR_MAP[DEBUG_COLOUR_KEY]

INTERSECTION_1_EDGE_ID_KEY = "edge-1-id"
INTERSECTION_1_X_KEY = "edge-1-x"
INTERSECTION_2_EDGE_ID_KEY = "edge-2-id"
INTERSECTION_2_X_KEY = "edge-2-x"
INTERSECTION_COLOUR_KEY = "intersection-colour"
INTERSECTION_WALL_ID = "intersection-wall-id"
INTERSECTION_X_KEY = "intersection-x"
INTERSECTION_IS_BEGINNING_KEY = "intersection-is-beginning"


def identity_function(v):
	return v
