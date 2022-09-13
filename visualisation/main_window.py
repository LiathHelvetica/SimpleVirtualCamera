from properties import WINDOW_X_SIZE, WINDOW_Y_SIZE, PROJECT_NAME, RESIZABLE, WITH_SURFACE_REMOVAL
from pyglet.window import Window
from graphics_helpers.command_store import update_command_store
from graphics_helpers.stage_creator import create_stage
from graphics_helpers.stage_painter import paint_without_surface_removal, paint_with_surface_removal
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
		entities_2d = create_stage(self.entities)
		self.clear()
		if WITH_SURFACE_REMOVAL:
			paint_with_surface_removal(self.entities, entities_2d, self.width, self.height)
			return
		paint_without_surface_removal(entities_2d, self.width, self.height)
