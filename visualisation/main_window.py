from properties import WINDOW_X_SIZE, WINDOW_Y_SIZE, PROJECT_NAME, RESIZABLE
from pyglet.window import Window
from graphics_helpers.camera_parameters_store import update_store, is_proper_command
from graphics_helpers.stage_creator import create_stage
from graphics_helpers.stage_painter import paint


class MainWindow(Window):
	def __init__(self):
		super(MainWindow, self).__init__(
			WINDOW_X_SIZE,
			WINDOW_Y_SIZE,
			visible=False,
			caption=PROJECT_NAME,
			resizable=RESIZABLE
		)
		self.set_visible()

	def on_key_press(self, key, modifiers):
		if is_proper_command(key):
			update_store(key)

	def on_draw(self):
		self.clear()
		x_c = self.width // 2
		y_c = self.height // 2
		entities = create_stage(x_c, y_c)
		paint(entities, x_c, y_c)
