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


def map_to_edge_colour(key):
	return *COLOUR_MAP[key], *COLOUR_MAP[key]


def map_to_point_colour(key):
	return COLOUR_MAP[key]
