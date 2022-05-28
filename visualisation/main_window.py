from properties import WINDOW_X_SIZE, WINDOW_Y_SIZE, PROJECT_NAME, RESIZABLE, WITH_SURFACE_REMOVAL
from pyglet.window import Window
from graphics_helpers.command_store import update_command_store
from graphics_helpers.stage_creator import create_stage
from graphics_helpers.stage_painter import paint, paint_with_surface_removal
from entity_store import ENTITY_STORE


class MainWindow(Window):
	def __init__(self):
		self.entities = None
		self.reset_entities()
		super(MainWindow, self).__init__(
			WINDOW_X_SIZE,
			WINDOW_Y_SIZE,
			visible=False,
			caption=PROJECT_NAME,
			resizable=RESIZABLE
		)
		self.set_visible()

	def reset_entities(self):
		self.entities = ENTITY_STORE.copy()

	def on_key_press(self, key, modifiers):
		update_command_store(key, self)

	def on_draw(self):
		x_c = self.width // 2
		y_c = self.height // 2
		entities_2d = create_stage(self.entities)
		self.clear()
		if WITH_SURFACE_REMOVAL:
			# TODO: delete later
			paint(entities_2d, x_c, y_c)
			paint_with_surface_removal(entities_2d, self.entities, x_c, y_c)
		else:
			paint(entities_2d, x_c, y_c)
