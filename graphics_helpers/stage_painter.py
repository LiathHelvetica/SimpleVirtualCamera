from pyglet.graphics import Batch
from pyglet.gl import GL_LINES


def paint(entities, x_c, y_c):
	batch = Batch()
	for _, edge in entities.edges.items():
		p1, p2 = edge.get_point_pair(entities)
		batch.add(2, GL_LINES, None, (
			"v2i", (p1.x + x_c, p1.y + y_c, p2.x + x_c, p2.y + y_c)
		), (
			"c3B", edge.get_colour()
		))
	batch.draw()
