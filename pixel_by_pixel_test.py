from visualisation.main_window import MainWindow
from pyglet.app import run
from properties import WINDOW_X_SIZE, WINDOW_Y_SIZE, PROJECT_NAME, RESIZABLE, COLOUR_MAP, DEFAULT_COLOUR
from pyglet.window import Window
from graphics_helpers.command_store import update_command_store
from graphics_helpers.stage_creator import create_stage
from graphics_helpers.stage_painter import paint, paint_with_surface_removal
from entity_store import ENTITY_STORE
from pyglet.window.key import UP, DOWN, LEFT, RIGHT
from pyglet.graphics import Batch
from pyglet.gl import GL_LINES, GL_POINTS


class MWindow(Window):
	def __init__(self):
		self.colour = COLOUR_MAP[DEFAULT_COLOUR]
		super(MWindow, self).__init__(
			WINDOW_X_SIZE,
			WINDOW_Y_SIZE,
			visible=False,
			caption=PROJECT_NAME,
			resizable=RESIZABLE
		)
		self.set_visible()

	def on_key_press(self, key, modifiers):
		if key == UP:
			self.colour = COLOUR_MAP["green"]
		elif key == DOWN:
			self.colour = COLOUR_MAP["yellow"]
		elif key == LEFT:
			self.colour = COLOUR_MAP["blue"]
		elif key == RIGHT:
			self.colour = COLOUR_MAP["red"]
		else:
			self.colour = COLOUR_MAP[DEFAULT_COLOUR]

	def on_draw(self):
		batch = Batch()
		v_list = []
		c_list = []
		n = 0
		for x in range(self.width):
			for y in range(self.height):
				v_list.append(x)
				v_list.append(y)
				c_list.append(self.colour[0])
				c_list.append(self.colour[1])
				c_list.append(self.colour[2])
				n += 1
		batch.add(n, GL_POINTS, None, (
			"v2i", v_list
		), (
			"c3B", c_list
		))
		batch.draw()


main_window = MWindow()
run()
