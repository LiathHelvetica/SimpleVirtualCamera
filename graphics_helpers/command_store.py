from properties import SHIFT_QUANTUM, ROTATION_QUANTUM, ZOOM_QUANTUM, identity_function
from pyglet.window.key import A, D, S, W, SPACE, LSHIFT, J, L, I, K, U, O, ESCAPE
from graphics_helpers.stage_creator import transform_point, create_shift_x_matrix, create_shift_y_matrix, \
	create_shift_z_matrix, create_x_rotation_matrix, create_y_rotation_matrix, create_z_rotation_matrix
from properties import ZOOM_UP_KEY, ZOOM_DOWN_KEY


class CommandStore:
	def __init__(self):
		self.get_new_point = identity_function
		self.last_pressed_key = None
		self.zoom_factor = 1.0

	def zoom_command_was_committed(self):
		return self.last_pressed_key == ZOOM_UP_KEY or self.last_pressed_key == ZOOM_DOWN_KEY


COMMAND_STORE = CommandStore()


def create_command(get_matrix, quantum):
	def outcome(point):
		return transform_point(get_matrix(quantum), point)
	return outcome


KEY_TO_COMMAND_MAP = {
	D: create_command(create_shift_x_matrix, SHIFT_QUANTUM),
	A: create_command(create_shift_x_matrix, -SHIFT_QUANTUM),
	W: create_command(create_shift_y_matrix, SHIFT_QUANTUM),
	S: create_command(create_shift_y_matrix, -SHIFT_QUANTUM),
	SPACE: create_command(create_shift_z_matrix, SHIFT_QUANTUM),
	LSHIFT: create_command(create_shift_z_matrix, -SHIFT_QUANTUM),
	L: create_command(create_y_rotation_matrix, ROTATION_QUANTUM),
	J: create_command(create_y_rotation_matrix, -ROTATION_QUANTUM),
	I: create_command(create_x_rotation_matrix, ROTATION_QUANTUM),
	K: create_command(create_x_rotation_matrix, -ROTATION_QUANTUM),
	U: create_command(create_z_rotation_matrix, -ROTATION_QUANTUM),
	O: create_command(create_z_rotation_matrix, ROTATION_QUANTUM),
	ZOOM_UP_KEY: identity_function,
	ZOOM_DOWN_KEY: identity_function
}


def update_command_store(key, main_window):
	COMMAND_STORE.last_pressed_key = key
	if key == ESCAPE:
		main_window.reset_entities()
	if key == ZOOM_UP_KEY:
		COMMAND_STORE.zoom_factor = COMMAND_STORE.zoom_factor * ZOOM_QUANTUM
	if key == ZOOM_DOWN_KEY:
		COMMAND_STORE.zoom_factor = COMMAND_STORE.zoom_factor * (1 / ZOOM_QUANTUM)
	command = KEY_TO_COMMAND_MAP[key] if key in KEY_TO_COMMAND_MAP else identity_function
	COMMAND_STORE.get_new_point = command
