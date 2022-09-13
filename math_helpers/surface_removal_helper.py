from entity_store import Point
from numpy import inf


def find_centroid(vertices_2d):
	sum_x = 0.0
	sum_y = 0.0
	n_points = len(vertices_2d)
	for vertex in vertices_2d:
		sum_x += vertex.x
		sum_y += vertex.y
	return Point(sum_x / n_points, sum_y / n_points, 0)


def find_bounding_box(vertices):
	x_min = inf
	x_max = -inf
	y_min = inf
	y_max = -inf
	for vertex in vertices:
		x = vertex.x
		y = vertex.y
		if x < x_min:
			x_min = x
		if y < y_min:
			y_min = y
		if x > x_max:
			x_max = x
		if y > y_max:
			y_max = y
	return y_max, y_min, x_max, x_min


def calculate_edge_function(p, v_a, v_b):
	return (p.x - v_a.x) * (v_b.y - v_a.y) - (p.y - v_a.y) * (v_b.x - v_a.x)


def calculate_point_z(v1, v2, v3, lambda_1, lambda_2, lambda_3):
	return 1 / ((1 / v1.z) * lambda_1 + (1 / v2.z) * lambda_2 + (1 / v3.z) * lambda_3)
