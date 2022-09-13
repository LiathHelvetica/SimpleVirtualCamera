from properties import COLOUR_MAP, BACKGROUND_COLOUR_KEY, SURFACE_REMOVAL_CURRENT_POINT_NAME
from math_helpers.surface_removal_helper import find_centroid, find_bounding_box, calculate_edge_function,\
	calculate_point_z
from entity_store import Point
from pyglet.graphics import Batch
from pyglet.gl import GL_LINES, GL_POINTS
from numpy import full, inf, arctan2, indices
from itertools import product


def paint_without_surface_removal(entities, image_width, image_height):
	x_c = image_width // 2
	y_c = image_height // 2
	batch = Batch()
	for _, edge in entities.edges.items():
		p1, p2 = edge.get_point_pair(entities)
		batch.add(2, GL_LINES, None, (
			"v2i", (p1.x + x_c, p1.y + y_c, p2.x + x_c, p2.y + y_c)
		), (
			"c3B", edge.get_colour()
		))
	batch.draw()


def paint_with_surface_removal(entities_3d, entities_2d, image_width, image_height):
	x_c = image_width // 2
	y_c = image_height // 2
	x_img_min = -x_c
	x_img_max = image_width - x_c
	y_img_min = -y_c
	y_img_max = image_height - y_c
	default_colour = COLOUR_MAP[BACKGROUND_COLOUR_KEY]
	z_buffer = full((image_height, image_width), inf, dtype=float)
	colour_buffer = full((image_height, image_width), default_colour, dtype=(int, len(default_colour)))
	for wall_id, wall in entities_2d.walls.items():
		vertices_ids_2d = list(wall.get_vertices(entities_2d))
		vertices_2d = list(map(lambda i: entities_2d.points[i], list(vertices_ids_2d)))
		centroid = find_centroid(vertices_2d)
		vertices_2d.sort(key=get_closure_for_clockwise_sorting(centroid))
		y_max, y_min, x_max, x_min = find_bounding_box(vertices_2d)
		x_min = x_min if x_min > x_img_min else x_img_min
		x_max = x_max + 1 if x_max < x_img_max else x_img_max
		y_min = y_min if y_min > y_img_min else y_img_min
		y_max = y_max + 1 if y_max < y_img_max else y_img_max
		for x, y in product(range(x_min, x_max), range(y_min, y_max)):
			p = Point(x, y, 0, SURFACE_REMOVAL_CURRENT_POINT_NAME)
			e_01 = calculate_edge_function(p, vertices_2d[0], vertices_2d[1])
			e_12 = calculate_edge_function(p, vertices_2d[1], vertices_2d[2])
			e_20 = calculate_edge_function(p, vertices_2d[2], vertices_2d[0])
			if e_01 >= 0 and e_12 >= 0 and e_20 >= 0:
				triangle_area = calculate_edge_function(vertices_2d[0], vertices_2d[1], vertices_2d[2])
				if triangle_area == 0:
					continue
				lambda_0 = e_12 / triangle_area
				lambda_1 = e_20 / triangle_area
				lambda_2 = e_01 / triangle_area
				z = calculate_point_z(vertices_2d[0], vertices_2d[1], vertices_2d[2], lambda_0, lambda_1, lambda_2)
				x = x + x_c
				y = y + y_c
				if z < z_buffer[y, x]:
					z_buffer[y, x] = z
					colour_buffer[y, x] = COLOUR_MAP[wall.colour]
	gl_points = indices((image_width, image_height)).transpose((2, 1, 0)).flatten()
	gl_colours = colour_buffer.flatten()
	batch = Batch()
	batch.add(image_height * image_width, GL_POINTS, None, (
		"v2i", gl_points
	), (
		"c3B", gl_colours
	))
	batch.draw()


def get_closure_for_clockwise_sorting(centroid):
	def atan(point):
		x = point.x - centroid.x
		y = point.y - centroid.y
		return -arctan2(y, x)
	return atan
