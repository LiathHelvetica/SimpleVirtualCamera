from properties import WINDOW_X_SIZE, WINDOW_Y_SIZE, PROJECT_NAME
from pyglet.window import Window

from pyglet.graphics import Batch
from pyglet.shapes import Line


class MainWindow(Window):
	def __init__(self):
		super(MainWindow, self).__init__(WINDOW_X_SIZE, WINDOW_Y_SIZE, visible=False, caption=PROJECT_NAME)
		self.set_visible()

	def on_key_press(self, symbol, modifiers):
		print(symbol)
		print(modifiers)

	def on_draw(self):
		# TEST
		batch = Batch()
		l1 = Line(100, 100, 200, 200, width=1, batch=batch)
		l2 = Line(400, 400, 600, 600, width=1, batch=batch)
		batch.draw()
