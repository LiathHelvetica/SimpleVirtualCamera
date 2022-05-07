from graphics_helpers.camera_parameters_store import CAMERA_PARAMETERS_STORE
from properties import X_SHIFT_KEY, Y_SHIFT_KEY, Z_SHIFT_KEY, X_ROTATION_KEY, Y_ROTATION_KEY, Z_ROTATION_KEY, ZOOM_KEY, TINY_NUMBER
from entity_store import ENTITY_STORE
from entity_store.point import Point
from math import sin, cos


def create_stage():
	entities = ENTITY_STORE.copy()
	for point_id, point in entities.points.items():
		new_point = point.to_vector()
		new_point = transform_point(
			create_shift_matrix(
				CAMERA_PARAMETERS_STORE[X_SHIFT_KEY],
				CAMERA_PARAMETERS_STORE[Y_SHIFT_KEY],
				CAMERA_PARAMETERS_STORE[Z_SHIFT_KEY]
			),
			new_point
		)
		new_point = transform_point(create_x_rotation_matrix(CAMERA_PARAMETERS_STORE[X_ROTATION_KEY]), new_point)
		new_point = transform_point(create_y_rotation_matrix(CAMERA_PARAMETERS_STORE[Y_ROTATION_KEY]), new_point)
		new_point = transform_point(create_z_rotation_matrix(CAMERA_PARAMETERS_STORE[Z_ROTATION_KEY]), new_point)
		new_point = transform_point(create_cast_matrix(CAMERA_PARAMETERS_STORE[ZOOM_KEY]), new_point)

		entities.points[point_id] = Point(new_point[0], new_point[1], new_point[2], point.id, entities)
	return entities


def transform_point(t_matrix, p):
	outcome = list(map(lambda row: sum([m_x * p_x for m_x, p_x in zip(row, p)]), t_matrix))
	return list(map(lambda x: x / outcome[3] if outcome[3] != 0.0 else TINY_NUMBER, outcome))


def create_shift_matrix(x, y, z):
	return [
		[1, 0, 0, x],
		[0, 1, 0, y],
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
	return [
		[1, 0, 0, 0],
		[0, 1, 0, 0],
		[0, 0, 0, 0],
		[0, 0, 1/d, 1]
	]
