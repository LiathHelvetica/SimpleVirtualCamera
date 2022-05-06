from pyglet.graphics import Batch
from pyglet.gl import GL_LINES


def paint(entities):
	batch = Batch()
	for _, edge in entities.edges.items():
		p1, p2 = edge.get_point_pair(entities)
		# print(f"${[p1.x, p1.y, p2.x, p2.y]}")
		batch.add(2, GL_LINES, None, ("v2i", (p1.x, p1.y, p2.x, p2.y)))
	# print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
	batch.draw()
