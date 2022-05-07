from properties import X_SHIFT_KEY, Y_SHIFT_KEY, Z_SHIFT_KEY, X_ROTATION_KEY, Y_ROTATION_KEY, Z_ROTATION_KEY, \
	ZOOM_KEY, SHIFT_QUANTUM, ROTATION_QUANTUM, ZOOM_QUANTUM, INITIAL_X_SHIFT, INITIAL_Y_SHIFT, INITIAL_Z_SHIFT, \
	INITIAL_X_ROTATION, INITIAL_Y_ROTATION, INITIAL_Z_ROTATION, INITIAL_ZOOM
from pyglet.window.key import A, D, S, W, SPACE, LSHIFT, J, L, I, K, U, O, UP, DOWN, ESCAPE


class CameraParametersStore:
	def __init__(self):
		self.store = None
		self.create_new_store()

	def create_new_store(self):
		self.store = {
			X_SHIFT_KEY: INITIAL_X_SHIFT,
			Y_SHIFT_KEY: INITIAL_Y_SHIFT,
			Z_SHIFT_KEY: INITIAL_Z_SHIFT,
			X_ROTATION_KEY: INITIAL_X_ROTATION,
			Y_ROTATION_KEY: INITIAL_Y_ROTATION,
			Z_ROTATION_KEY: INITIAL_Z_ROTATION,
			ZOOM_KEY: INITIAL_ZOOM
		}


CAMERA_PARAMETERS_STORE = CameraParametersStore()


def create_update_function(key, quantum):
	def outcome():
		CAMERA_PARAMETERS_STORE.store[key] = CAMERA_PARAMETERS_STORE.store[key] + quantum
	return outcome


def reset_camera_parameter_store():
	CAMERA_PARAMETERS_STORE.create_new_store()


KEY_TO_UPDATE_FUNCTION_MAP = {
	D: create_update_function(X_SHIFT_KEY, SHIFT_QUANTUM),
	A: create_update_function(X_SHIFT_KEY, -SHIFT_QUANTUM),
	W: create_update_function(Y_SHIFT_KEY, SHIFT_QUANTUM),
	S: create_update_function(Y_SHIFT_KEY, -SHIFT_QUANTUM),
	SPACE: create_update_function(Z_SHIFT_KEY, SHIFT_QUANTUM),
	LSHIFT: create_update_function(Z_SHIFT_KEY, -SHIFT_QUANTUM),
	L: create_update_function(Y_ROTATION_KEY, ROTATION_QUANTUM),
	J: create_update_function(Y_ROTATION_KEY, -ROTATION_QUANTUM),
	I: create_update_function(X_ROTATION_KEY, ROTATION_QUANTUM),
	K: create_update_function(X_ROTATION_KEY, -ROTATION_QUANTUM),
	U: create_update_function(Z_ROTATION_KEY, -ROTATION_QUANTUM),
	O: create_update_function(Z_ROTATION_KEY, ROTATION_QUANTUM),
	UP: create_update_function(ZOOM_KEY, ZOOM_QUANTUM),
	DOWN: create_update_function(ZOOM_KEY, -ZOOM_QUANTUM),
	ESCAPE: reset_camera_parameter_store
}


def update_store(key):
	KEY_TO_UPDATE_FUNCTION_MAP[key]()


def is_proper_command(key):
	return key in KEY_TO_UPDATE_FUNCTION_MAP
