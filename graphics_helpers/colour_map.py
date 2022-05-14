from properties import COLOUR_MAP


def map_to_edge_colour(key):
	return *COLOUR_MAP[key], *COLOUR_MAP[key]
