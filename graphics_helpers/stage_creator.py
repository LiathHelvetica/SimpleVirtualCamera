from graphics_helpers.camera_parameters_store import CAMERA_PARAMETERS_STORE
from properties import X_SHIFT_KEY, Y_SHIFT_KEY, Z_SHIFT_KEY, X_ROTATION_KEY, Y_ROTATION_KEY, Z_ROTATION_KEY, ZOOM_KEY, TINY_NUMBER
from entity_store import ENTITY_STORE
from entity_store.point import Point
from math import sin, cos


def create_stage(x_c, y_c):
	entities = ENTITY_STORE.copy()
	return transform_store(entities, x_c, y_c)


def transform_store(entities, x_c, y_c):
	for point_id, point in entities.points.items():
		new_point = point.to_vector()
		camera_parameters_store = CAMERA_PARAMETERS_STORE.store
		new_point = shift_with_angle(camera_parameters_store, new_point)
		new_point = rotate_with_shift(camera_parameters_store, new_point, create_x_rotation_matrix, X_ROTATION_KEY)
		new_point = rotate_with_shift(camera_parameters_store, new_point, create_y_rotation_matrix, Y_ROTATION_KEY)
		new_point = rotate_with_shift(camera_parameters_store, new_point, create_z_rotation_matrix, Z_ROTATION_KEY)

		# new_point = shift(camera_parameters_store, new_point, direction=1)
		new_point = transform_point(create_cast_matrix(camera_parameters_store[ZOOM_KEY]), new_point)
		# new_point = shift(camera_parameters_store, new_point, direction=-1)

		new_point = transform_point(create_shift_matrix(x_c, y_c,	0), new_point)

		entities.points[point_id] = Point(new_point[0], new_point[1], new_point[2], point.id, entities)
	return entities


def transform_point(t_matrix, p):
	outcome = list(map(lambda row: sum([m_x * p_x for m_x, p_x in zip(row, p)]), t_matrix))
	return list(map(lambda x: x / (outcome[3] if outcome[3] != 0.0 else TINY_NUMBER), outcome))


def rotate(camera_parameters_store, new_point, direction=1):
	new_point = transform_point(create_x_rotation_matrix(camera_parameters_store[X_ROTATION_KEY] * direction), new_point)
	new_point = transform_point(create_y_rotation_matrix(camera_parameters_store[Y_ROTATION_KEY] * direction), new_point)
	new_point = transform_point(create_z_rotation_matrix(camera_parameters_store[Z_ROTATION_KEY] * direction), new_point)
	return new_point


def shift_with_angle(camera_parameters_store, new_point):
	new_point = rotate(camera_parameters_store, new_point, direction=-1)
	new_point = shift(camera_parameters_store, new_point)
	new_point = rotate(camera_parameters_store, new_point, direction=1)
	return new_point


def shift(camera_parameters_store, new_point, direction=1):
	return transform_point(
			create_shift_matrix(
				camera_parameters_store[X_SHIFT_KEY] * direction,
				camera_parameters_store[Y_SHIFT_KEY] * direction,
				camera_parameters_store[Z_SHIFT_KEY] * direction
			),
			new_point
		)


def rotate_with_shift(camera_parameters_store, new_point, get_rotation_matrix, rotation_key):
	new_point = shift(camera_parameters_store, new_point, direction=1)
	new_point = transform_point(get_rotation_matrix(camera_parameters_store[rotation_key]), new_point)
	new_point = shift(camera_parameters_store, new_point, direction=-1)
	return new_point


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
	d = TINY_NUMBER if d == 0.0 else d
	return [
		[1, 0, 0, 0],
		[0, 1, 0, 0],
		[0, 0, 0, 0],
		[0, 0, 1/d, 1]
	]
