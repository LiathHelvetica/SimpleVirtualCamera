from properties import X_SHIFT_KEY, Y_SHIFT_KEY, Z_SHIFT_KEY, X_ROTATION_KEY, Y_ROTATION_KEY, Z_ROTATION_KEY, \
	ZOOM_KEY, SHIFT_QUANTUM, ROTATION_QUANTUM, ZOOM_QUANTUM
from pyglet.window.key import A, D, S, W, SPACE, LSHIFT, J, L, I, K, U, O, UP, DOWN

CAMERA_PARAMETERS_STORE = {
	X_SHIFT_KEY: 0,
	Y_SHIFT_KEY: 0,
	Z_SHIFT_KEY: 0,
	X_ROTATION_KEY: 0,
	Y_ROTATION_KEY: 0,
	Z_ROTATION_KEY: 0,
	ZOOM_KEY: 30
}


def create_update_function(key, quantum):
	def outcome():
		CAMERA_PARAMETERS_STORE[key] = CAMERA_PARAMETERS_STORE[key] + quantum
	return outcome


KEY_TO_UPDATE_FUNCTION_MAP = {
	D: create_update_function(X_SHIFT_KEY, SHIFT_QUANTUM),
	A: create_update_function(X_SHIFT_KEY, -SHIFT_QUANTUM),
	W: create_update_function(Y_SHIFT_KEY, SHIFT_QUANTUM),
	S: create_update_function(Y_SHIFT_KEY, -SHIFT_QUANTUM),
	SPACE: create_update_function(Z_SHIFT_KEY, SHIFT_QUANTUM),
	LSHIFT: create_update_function(Z_SHIFT_KEY, -SHIFT_QUANTUM),
	L: create_update_function(X_ROTATION_KEY, ROTATION_QUANTUM),
	J: create_update_function(X_ROTATION_KEY, -ROTATION_QUANTUM),
	I: create_update_function(Y_ROTATION_KEY, ROTATION_QUANTUM),
	K: create_update_function(Y_ROTATION_KEY, -ROTATION_QUANTUM),
	U: create_update_function(Z_ROTATION_KEY, -ROTATION_QUANTUM),
	O: create_update_function(Z_ROTATION_KEY, ROTATION_QUANTUM),
	UP: create_update_function(ZOOM_KEY, ZOOM_QUANTUM),
	DOWN: create_update_function(ZOOM_KEY, -ZOOM_QUANTUM)
}


def update_store(key):
	KEY_TO_UPDATE_FUNCTION_MAP[key]()


def is_proper_command(key):
	return key in KEY_TO_UPDATE_FUNCTION_MAP
