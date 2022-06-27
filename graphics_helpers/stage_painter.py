from pyglet.graphics import Batch
from pyglet.gl import GL_LINES, GL_POINTS
from properties import INTERSECTION_1_X_KEY, INTERSECTION_2_X_KEY, INTERSECTION_COLOUR_KEY, INTERSECTION_WALL_ID, \
	INTERSECTION_X_KEY, SHIFT_OF_OBSERVER, TINY_NUMBER, DEBUG_INTERSECTIONS, DEBUG_COLOUR, INTERSECTION_IS_BEGINNING_KEY
from graphics_helpers.colour_map import map_to_edge_colour
from numpy import array, sqrt


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


def paint_with_surface_removal(entities_2d, entities, x_c, y_c):
	batch = Batch()
	y_sorted_2d_edges = list(entities_2d.edges.values())
	y_sorted_2d_edges.sort(key=get_edge_sorting_function(entities_2d), reverse=True)
	active_walls = set()
	for scan_y in range(y_c, -y_c - 1, -1):
		update_active_walls(active_walls, scan_y, y_sorted_2d_edges, entities_2d)
		scan_intersections = []
		deactivated_walls = set()
		for wall_id in active_walls:
			intersections_data = find_wall_with_scan_intersections(scan_y, wall_id, entities_2d)
			if intersections_data is None:
				deactivated_walls.add(wall_id)
			else:
				x_1 = intersections_data[INTERSECTION_1_X_KEY]
				x_2 = intersections_data[INTERSECTION_2_X_KEY]
				is_x_1_before_x_2 = x_1 < x_2
				scan_intersections.append(
					create_scan_intersection_object(
						x_1,
						intersections_data,
						entities_2d,
						is_x_1_before_x_2
					)
				)
				scan_intersections.append(
					create_scan_intersection_object(
						x_2,
						intersections_data,
						entities_2d,
						not is_x_1_before_x_2
					)
				)
		active_walls.difference_update(deactivated_walls)
		if scan_intersections:
			scan_intersections.sort(key=lambda v: v[INTERSECTION_X_KEY] - 0.5 * v[INTERSECTION_IS_BEGINNING_KEY])
			paint_scan(scan_y, scan_intersections, entities, entities_2d, x_c, y_c, batch)

	batch.draw()


def get_edge_sorting_function(entity_store):
	def outcome(edge):
		return edge.get_higher_vertex(entity_store).y
	return outcome


def update_active_walls(active_walls, scan_y, y_sorted_2d_edges, entities_2d):
	n_popped_edges = 0
	for edge in y_sorted_2d_edges:
		if is_edge_scanned(scan_y, edge, entities_2d):
			active_walls.update(edge.walls)
			n_popped_edges += 1
		else:
			break
	for _ in range(n_popped_edges):
		y_sorted_2d_edges.pop(0)


def is_edge_scanned(scan_y, edge, entities_2d):
	v_1, v_2 = edge.get_y_ordered_vertices(entities_2d)
	return v_1.y >= scan_y >= v_2.y


def find_wall_with_scan_intersections(scan_y, wall_id, entities_2d):
	outcome_edges = []
	for edge_id in entities_2d.walls[wall_id].edges_ids:
		v_1, v_2 = entities_2d.edges[edge_id].get_point_pair(entities_2d)
		if (v_1.y <= scan_y <= v_2.y) or (v_2.y <= scan_y <= v_1.y):
			outcome_edges.append(edge_id)
	intersection_points = get_intersection_points_x(outcome_edges, entities_2d, scan_y)
	n_intersections = len(intersection_points)
	assert n_intersections <= 2
	return None if n_intersections == 0 else {
		INTERSECTION_1_X_KEY: intersection_points[0],
		INTERSECTION_2_X_KEY: intersection_points[0],
		INTERSECTION_COLOUR_KEY: entities_2d.edges[outcome_edges[0]].get_colour(),
		INTERSECTION_WALL_ID: wall_id
	} if n_intersections == 1 else {
		INTERSECTION_1_X_KEY: intersection_points[0],
		INTERSECTION_2_X_KEY: intersection_points[1],
		INTERSECTION_COLOUR_KEY: entities_2d.edges[outcome_edges[0]].get_colour(),
		INTERSECTION_WALL_ID: wall_id
	}


def get_intersection_points_x(outcome_edges, entities_2d, scan_y):
	intersection_x = set()
	for edge_id in outcome_edges:
		edge = entities_2d.edges[edge_id]
		v_1, v_2 = edge.get_point_pair(entities_2d)
		if round(v_1.y) == round(v_2.y):
			intersection_x.add(round(v_1.x))
			intersection_x.add(round(v_2.x))
		elif round(v_1.x) == round(v_2.x):
			intersection_x.add(round(v_1.x))
		else:
			a = (v_1.y - v_2.y) / (v_1.x - v_2.x)
			b = v_1.y - v_1.x * a
			intersection_x.add(round((scan_y - b) / a))
	return list(intersection_x)


def create_scan_intersection_object(x, intersections_data, entities, is_beginning):
	return {
		INTERSECTION_X_KEY: x,
		INTERSECTION_COLOUR_KEY: entities.walls[intersections_data[INTERSECTION_WALL_ID]].get_colour(),
		INTERSECTION_WALL_ID: intersections_data[INTERSECTION_WALL_ID],
		INTERSECTION_IS_BEGINNING_KEY: is_beginning
	}


def paint_scan(scan_y, scan_intersections, entities, entities_2d, x_c, y_c, batch):
	active_walls = {}
	# n_scan_intersections = len(scan_intersections)
	# i = 0
	scan_x = update_active_walls_for_scan(active_walls, scan_intersections)
	while scan_intersections:
		# current_colour = get_colour_of_nearest_wall(active_walls, entities, scan_y)
		from_x = scan_x
		to_x = scan_intersections[0][INTERSECTION_X_KEY]
		fragment_center_x = (to_x + from_x) / 2
		# TODO: The error is in distance function
		# current_colour = get_colour_of_nearest_wall_2(active_walls, entities, scan_y, fragment_center_x)
		# current_colour = get_colour_of_nearest_wall(active_walls, entities, scan_y)
		current_colour = get_colour_of_nearest_wall_3(active_walls, entities, scan_y, fragment_center_x)
		if current_colour is not None:
			batch.add(2, GL_LINES, None, (
				"v2i", (round(from_x + x_c), round(scan_y + y_c), round(to_x + x_c), round(scan_y + y_c))
			), (
				"c3B", current_colour
			))
		scan_x = update_active_walls_for_scan(active_walls, scan_intersections)

	# if DEBUG_INTERSECTIONS:
		# add_intersections_to_batch(batch, scan_intersections, scan_y, x_c, y_c)


def update_active_walls_for_scan(active_walls, scan_intersections):
	current_x = scan_intersections[0][INTERSECTION_X_KEY]
	current_tag = scan_intersections[0][INTERSECTION_IS_BEGINNING_KEY]
	intersections_to_pop = 0
	for intersection in scan_intersections:
		if intersection[INTERSECTION_X_KEY] == current_x and intersection[INTERSECTION_IS_BEGINNING_KEY] == current_tag:
			if intersection[INTERSECTION_IS_BEGINNING_KEY]:
				active_walls[intersection[INTERSECTION_WALL_ID]] = intersection
			else:
				del active_walls[intersection[INTERSECTION_WALL_ID]]
			intersections_to_pop += 1
		else:
			break

	for _ in range(intersections_to_pop):
		scan_intersections.pop(0)

	return current_x


def add_intersections_to_batch(batch, scan_intersections, scan_y, x_c, y_c):
	for intersection in scan_intersections:
		batch.add(1, GL_POINTS, None, (
			"v2i", (intersection[INTERSECTION_X_KEY] + x_c, scan_y + y_c)
		), (
			"c3B", DEBUG_COLOUR
		))


def get_colour_of_nearest_wall_2(active_walls, entities, scan_y, x):
	best_colour = None
	shortest_distance = float("inf")
	for wall_id, wall_intersection in active_walls.items():
		a, b, c, d = get_plane_equation(wall_id, entities)
		# current_distance = calculate_distance_to_pierce(a, b, c, d, scan_y, x)
		c = c if abs(c) > 0.0000000000001 else 0.0000000000001
		current_distance = abs((d - a * x - b * scan_y) / c)
		if current_distance < shortest_distance:
			best_colour = wall_intersection[INTERSECTION_COLOUR_KEY]
			shortest_distance = current_distance
	return best_colour


def get_colour_of_nearest_wall_3(active_walls, entities, scan_y, x):
	best_colour = None
	shortest_distance = float("inf")
	for wall_id, wall_intersection in active_walls.items():
		a, b, c, d = get_plane_equation(wall_id, entities)
		current_distance = calculate_distance_to_pierce_5(a, b, c, d, scan_y, x)
		if current_distance < shortest_distance:
			best_colour = wall_intersection[INTERSECTION_COLOUR_KEY]
			shortest_distance = current_distance
	return best_colour


def get_colour_of_nearest_wall(active_walls, entities, scan_y):
	best_colour = None
	shortest_distance = float("inf")
	for wall_id, wall_intersection in active_walls.items():
		a, b, c, d = get_plane_equation(wall_id, entities)
		current_distance = calculate_distance_to_pierce_5(a, b, c, d, scan_y, wall_intersection[INTERSECTION_X_KEY])
		if current_distance < shortest_distance:
			best_colour = wall_intersection[INTERSECTION_COLOUR_KEY]
			shortest_distance = current_distance
	return best_colour


def get_plane_equation(wall_id, entities):
	edges = []
	i = 1
	for edge_id in entities.walls[wall_id].edges_ids:
		edges.append(edge_id)
		if i == 2:
			break
		i += 1
	v_a, v_b, v_c = get_vertices_from_2_edges(edges[0], edges[1], entities)
	a = (v_b.y - v_a.y) * (v_c.z - v_a.z) - (v_c.y - v_a.y) * (v_b.z - v_a.z)
	b = (v_b.z - v_a.z) * (v_c.x - v_a.x) - (v_c.z - v_a.z) * (v_b.x - v_a.x)
	c = (v_b.x - v_a.x) * (v_c.y - v_a.y) - (v_c.x - v_a.x) * (v_b.y - v_a.y)
	d = -(a * v_a.x + b * v_a.y + c * v_a.z)
	return a, b, c, d


def get_vertices_from_2_edges(edge_id_1, edge_id_2, entities):
	v_a, v_b = entities.edges[edge_id_1].get_point_pair(entities)
	v_d, v_e = entities.edges[edge_id_2].get_point_pair(entities)
	v_c = v_d if v_d.id != v_a.id and v_d.id != v_b.id else v_e
	return v_a, v_b, v_c


def calculate_distance_to_pierce(a, b, c, d, y, x):
	t_div = x + y + SHIFT_OF_OBSERVER
	t_div = TINY_NUMBER if t_div == 0.0 else t_div
	t = d + c * SHIFT_OF_OBSERVER
	x_target = t * x
	y_target = t * y
	z_target = SHIFT_OF_OBSERVER * (t - 1)
	return x_target ** 2 + y_target ** 2 + (z_target + SHIFT_OF_OBSERVER) ** 2


def calculate_distance_to_pierce_3(a, b, c, d, y, x):
	l_b = array([0, 0, -SHIFT_OF_OBSERVER])
	l_a = array([x, y, 0]) - l_b
	t = (d - a * l_b[0] - b * l_b[1] - c * l_b[2]) / (a * l_a[0] + b * l_a[1] + c * l_a[2])
	pierce_p = l_b + t * l_a
	return sqrt(pierce_p[0] ** 2 + pierce_p[1] ** 2 + (SHIFT_OF_OBSERVER + pierce_p[2]) ** 2)


def calculate_distance_to_pierce_4(a, b, c, d, y, x):
	l_b = array([x, y, -SHIFT_OF_OBSERVER])
	l_a = array([x, y, 0]) - l_b
	t = (d - a * l_b[0] - b * l_b[1] - c * l_b[2]) / (a * l_a[0] + b * l_a[1] + c * l_a[2])
	pierce_p = l_b + t * l_a
	return sqrt((pierce_p[0] - x) ** 2 + (pierce_p[1] - y) ** 2 + (pierce_p[2]) ** 2)


def calculate_distance_to_pierce_5(a, b, c, d, y, x):
	l_b = array([x, y, -SHIFT_OF_OBSERVER])
	l_a = array([x, y, 0]) - l_b
	t = (d - a * l_b[0] - b * l_b[1] - c * l_b[2]) / (a * l_a[0] + b * l_a[1] + c * l_a[2])
	pierce_p = l_b + t * l_a
	return sqrt(pierce_p[2] ** 2)
