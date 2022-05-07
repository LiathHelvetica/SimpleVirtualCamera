DEFAULT_COLOUR = "white"


COLOUR_MAP = {
	"green": (0, 255, 0),
	"red": (255, 0, 0),
	DEFAULT_COLOUR: (255, 255, 255)
}


def map_to_edge_colour(key):
	return *COLOUR_MAP[key], *COLOUR_MAP[key]


def map_to_point_colour(key):
	return COLOUR_MAP[key]
