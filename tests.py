from graphics_helpers.stage_painter import get_closure_for_clockwise_sorting
from math_helpers.surface_removal_helper import find_bounding_box, calculate_edge_function
from entity_store import Point


def points_are_sorted_clockwise_1():
	v1 = Point(-1, -1, 0, "v1")
	v2 = Point(-1, 1, 0, "v2")
	v3 = Point(1, 0, 0, "v3")
	fake_centroid = Point(0, 0, 0)
	vertices = [v2, v1, v3]

	vertices.sort(key=get_closure_for_clockwise_sorting(fake_centroid))

	assert(vertices[0] == v2)
	assert(vertices[1] == v3)


def points_are_sorted_clockwise_2():
	v1 = Point(-170, 55, 0, "v1")
	v2 = Point(-70, 70, 0, "v2")
	v3 = Point(-80, -10, 0, "v3")
	fake_centroid = Point(-140, 40, 0)
	vertices = [v3, v1, v2]

	vertices.sort(key=get_closure_for_clockwise_sorting(fake_centroid))

	assert(vertices[0] == v1)
	assert(vertices[1] == v2)


def finding_bound_box():
	v1 = Point(412, -123, 0)
	v2 = Point(52, -12, 23)
	v3 = Point(-33, 12, 0)
	vertices = [v1, v2, v3]

	y_max, y_min, x_max, x_min = find_bounding_box(vertices)

	assert(y_max == 12)
	assert(y_min == -123)
	assert(x_max == 412)
	assert(x_min == -33)


def testing_if_point_is_inside():
	v1 = Point(-170, 55, 0, "v1")
	v2 = Point(-70, 70, 0, "v2")
	v3 = Point(-80, -10, 0, "v3")
	p = Point(-140, 40, 0, "p")

	e_01 = calculate_edge_function(p, v1, v2)
	e_12 = calculate_edge_function(p, v2, v3)
	e_20 = calculate_edge_function(p, v3, v1)

	assert(e_01 > 0)
	assert(e_12 > 0)
	assert(e_20 > 0)


def testing_if_point_is_outside():
	v1 = Point(-170, 55, 0, "v1")
	v2 = Point(-70, 70, 0, "v2")
	v3 = Point(-80, -10, 0, "v3")
	p = Point(-200, 100, 0, "p")

	e_01 = calculate_edge_function(p, v1, v2)
	e_12 = calculate_edge_function(p, v2, v3)
	e_20 = calculate_edge_function(p, v3, v1)

	assert(e_01 < 0 or e_20 < 0 or e_12 < 0)


def calculating_triangle_area():
	error_margin = 0.1
	area = 36
	v1 = Point(-3, 3, 0, "v1")
	v2 = Point(3, -3, 0, "v2")
	v3 = Point(-3, -3, 0, "v3")

	expected_area = calculate_edge_function(v1, v2, v3)

	assert(area - error_margin < expected_area < area + error_margin)


points_are_sorted_clockwise_1()
points_are_sorted_clockwise_2()
finding_bound_box()
testing_if_point_is_inside()
testing_if_point_is_outside()
calculating_triangle_area()

from numpy import full, indices
colour_buffer = full((4, 3), (0, 0, 0), dtype=(int, 3))
colour_buffer[0, 1] = (1, 1, 1)
colour_buffer[1, 0] = (2, 2, 2)
colour_buffer = colour_buffer.flatten()

image_width = 3
image_height = 4
gl_points = indices((image_width, image_height)).transpose((2, 1, 0)).flatten()
print(gl_points)
