PROJECT_NAME = "Simple Virtual Camera"

ASSETS_PATH_FORMAT = "assets/{0}"
ASSETS_FILES = list(map(
	lambda file_name: ASSETS_PATH_FORMAT.format(file_name),
	["figure1.json"]
))

ENTITIES_KEY = "entities"
POINTS_KEY = "points"
EDGES_KEY = "edges"
WALLS_KEY = "walls"

X_KEY = "x"
Y_KEY = "y"
Z_KEY = "z"

WINDOW_X_SIZE = 700
WINDOW_Y_SIZE = 500
