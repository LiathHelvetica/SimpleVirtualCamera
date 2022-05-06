from properties import WINDOW_X_SIZE, WINDOW_Y_SIZE, PROJECT_NAME
from pyglet.window import Window
from graphics_helpers.camera_parameters_store import update_store, is_proper_command
from graphics_helpers.stage_creator import create_stage
from graphics_helpers.stage_painter import paint


class MainWindow(Window):
	def __init__(self):
		super(MainWindow, self).__init__(WINDOW_X_SIZE, WINDOW_Y_SIZE, visible=False, caption=PROJECT_NAME)
		self.set_visible()

	def on_key_press(self, key, modifiers):
		if is_proper_command(key):
			update_store(key)
			# self.on_draw()

	def on_draw(self):
		print("on draw")
		self.clear()
		entities = create_stage()
		paint(entities)
