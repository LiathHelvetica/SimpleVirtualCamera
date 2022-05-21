from properties import TINY_NUMBER, SHIFT_OF_OBSERVER
from entity_store.point import Point
from math import sin, cos


def create_stage(entities):
	from graphics_helpers.command_store import COMMAND_STORE

	entities_2d = entities.copy()
	for point_id, point in entities.points.items():
		new_point = point.to_vector()
		new_point = COMMAND_STORE.get_new_point(new_point)

		entities.points[point_id] = Point(new_point[0], new_point[1], new_point[2], point.id, entities)

		new_point = transform_point(create_cast_matrix(SHIFT_OF_OBSERVER), new_point)

		if COMMAND_STORE.zoom_command_was_committed():
			new_point = transform_point(create_zoom_matrix(COMMAND_STORE.zoom_factor), new_point)

		entities_2d.points[point_id] = Point(new_point[0], new_point[1], new_point[2], point.id, entities_2d)
	return entities_2d


def transform_point(t_matrix, p):
	outcome = list(map(lambda row: sum([m_x * p_x for m_x, p_x in zip(row, p)]), t_matrix))
	return list(map(lambda x: x / (outcome[3] if outcome[3] != 0.0 else TINY_NUMBER), outcome))


def create_shift_matrix(x, y, z):
	return [
		[1, 0, 0, x],
		[0, 1, 0, y],
		[0, 0, 1, z],
		[0, 0, 0, 1]
	]


def create_shift_x_matrix(x):
	return [
		[1, 0, 0, x],
		[0, 1, 0, 0],
		[0, 0, 1, 0],
		[0, 0, 0, 1]
	]


def create_shift_y_matrix(y):
	return [
		[1, 0, 0, 0],
		[0, 1, 0, y],
		[0, 0, 1, 0],
		[0, 0, 0, 1]
	]


def create_shift_z_matrix(z):
	return [
		[1, 0, 0, 0],
		[0, 1, 0, 0],
		[0, 0, 1, z],
		[0, 0, 0, 1]
	]


def create_x_rotation_matrix(phi):
	return [
		[1, 0, 0, 0],
		[0, cos(phi), -sin(phi), 0],
		[0, sin(phi), cos(phi), 0],
		[0, 0, 0, 1]
	]


def create_y_rotation_matrix(phi):
	return [
		[cos(phi), 0, sin(phi), 0],
		[0, 1, 0, 0],
		[-sin(phi), 0, cos(phi), 0],
		[0, 0, 0, 1]
	]


def create_z_rotation_matrix(phi):
	return [
		[cos(phi), -sin(phi), 0, 0],
		[sin(phi), cos(phi), 0, 0],
		[0, 0, 1, 0],
		[0, 0, 0, 1]
	]


def create_cast_matrix(d):
	d = TINY_NUMBER if d == 0.0 else d
	return [
		[1, 0, 0, 0],
		[0, 1, 0, 0],
		[0, 0, 0, 0],
		[0, 0, 1/d, 1]
	]


def create_zoom_matrix(v):
	return [
		[v, 0, 0, 0],
		[0, v, 0, 0],
		[0, 0, v, 0],
		[0, 0, 0, 1]
	]
