from properties import SHOW_CENTER, CENTER_COLOUR, CENTER_COORDINATES, CENTER_ID
from graphics_helpers.colour_map import map_to_point_colour
from graphics_helpers.stage_creator import transform_store
from entity_store import Point
from entity_store import EntityStore
from pyglet.graphics import Batch
from pyglet.gl import GL_LINES, GL_POINTS


def paint(entities, x_c, y_c):
	batch = Batch()
	for _, edge in entities.edges.items():
		p1, p2 = edge.get_point_pair(entities)
		batch.add(2, GL_LINES, None, (
			"v2i", (p1.x + x_c, p1.y + y_c, p2.x + x_c, p2.y + y_c)
		), (
			"c3B", edge.get_colour()
		))
	if SHOW_CENTER:
		paint_center(batch, x_c, y_c)
	batch.draw()


def paint_center(batch, x_c, y_c):
	centers_store = EntityStore()
	Point(*CENTER_COORDINATES, CENTER_ID, centers_store)
	centers_store = transform_store(centers_store)
	for _, point in centers_store.points.items():
		batch.add(1, GL_POINTS, None, ("v2i", (point.x + x_c, point.y + y_c)), ("c3B", map_to_point_colour(CENTER_COLOUR)))

