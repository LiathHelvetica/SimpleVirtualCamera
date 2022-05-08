from math import pi

PROJECT_NAME = "Simple Virtual Camera"

ASSETS_PATH_FORMAT = "assets/{0}"
FIGURE_FILES = ["figure1.json"]
ASSETS_FILES = list(map(
	lambda file_name: ASSETS_PATH_FORMAT.format(file_name),
	FIGURE_FILES
))

ENTITIES_KEY = "entities"
POINTS_KEY = "points"
EDGES_KEY = "edges"
WALLS_KEY = "walls"
EDGE_DATA_KEY = "data"
EDGE_COLOUR_KEY = "colour"

X_KEY = "x"
Y_KEY = "y"
Z_KEY = "z"

WINDOW_X_SIZE = 700
WINDOW_Y_SIZE = 500

X_SHIFT_KEY = "X_SHIFT"
Y_SHIFT_KEY = "Y_SHIFT"
Z_SHIFT_KEY = "Z_SHIFT"

X_ROTATION_KEY = "X_ROTATION"
Y_ROTATION_KEY = "Y_ROTATION"
Z_ROTATION_KEY = "Z_ROTATION"

ZOOM_KEY = "ZOOM"

INITIAL_X_SHIFT = 0
INITIAL_Y_SHIFT = 0
INITIAL_Z_SHIFT = 0
INITIAL_X_ROTATION = 0
INITIAL_Y_ROTATION = 0
INITIAL_Z_ROTATION = 0
INITIAL_ZOOM = 300

SHIFT_QUANTUM = 10
ROTATION_QUANTUM = pi / 30
ZOOM_QUANTUM = 30

TINY_NUMBER = 0.00000000000000001

DEFAULT_COLOUR = "white"

COLOUR_MAP = {
	"green": (0, 255, 0),
	"l-green": (170, 255, 170),
	"red": (255, 0, 0),
	"l-red": (255, 170, 170),
	"blue": (0, 0, 255),
	"l-blue": (170, 170, 255),
	"magenta": (255, 0, 255),
	DEFAULT_COLOUR: (255, 255, 255)
}

SHOW_CENTER = True
CENTER_COLOUR = "magenta"
CENTER_COORDINATES = (0, 0, 0)
CENTER_ID = "center"

"wady, stack, "
