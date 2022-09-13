from math import pi
from pyglet.window.key import UP, DOWN

PROJECT_NAME = "Simple Virtual Camera"

ASSETS_PATH_FORMAT = "assets/{0}"
FIGURE_FILES = ["figure3.json"]
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
WALL_DATA_KEY = "data"
WALL_COLOUR_KEY = "colour"
WALL_EDGE_COLOUR_KEY = "edge-colour"

X_KEY = "x"
Y_KEY = "y"
Z_KEY = "z"

WINDOW_X_SIZE = 700
WINDOW_Y_SIZE = 500

SHIFT_OF_OBSERVER = 600

SHIFT_QUANTUM = 100
ROTATION_QUANTUM = pi / 15
ZOOM_QUANTUM = 1.1

TINY_NUMBER = 0.00000000000000001

DEFAULT_COLOUR = "white"
DEFAULT_EDGE_COLOUR = "magenta"
BACKGROUND_COLOUR_KEY = "black"

COLOUR_MAP = {
	"green": (0, 255, 0),
	"l-green": (170, 255, 170),
	"red": (255, 0, 0),
	"l-red": (255, 170, 170),
	"blue": (0, 0, 255),
	"l-blue": (170, 170, 255),
	"magenta": (255, 0, 255),
	"yellow": (255, 255, 0),
	DEFAULT_COLOUR: (255, 255, 255),
	BACKGROUND_COLOUR_KEY: (0, 0, 0)
}

ZOOM_UP_KEY = UP
ZOOM_DOWN_KEY = DOWN
DEFAULT_ZOOM = 1.0

WITH_SURFACE_REMOVAL = True
SURFACE_REMOVAL_CURRENT_POINT_NAME = "p"


def identity_function(v):
	return v
