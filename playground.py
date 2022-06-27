from numpy import array, column_stack
from numpy.linalg import solve
from properties import SHIFT_OF_OBSERVER


def calculate_distance_to_pierce_2(a, b, c, d, y, x):
	l_b = array([0, 0, -SHIFT_OF_OBSERVER])
	l_a = array([x, y, 0]) - l_b
	v_v = calculate_c_v(a, b, c, d)
	s_v, t_v = calculate_s_t(a, b, c)
	a = column_stack((l_a, -s_v, -t_v))
	b = v_v - l_b
	rst = solve(a, b)
	pierce_p = rst[1] * s_v + rst[2] * t_v + v_v
	print(pierce_p)
	return pierce_p[0] ** 2 + pierce_p[1] ** 2 + (SHIFT_OF_OBSERVER + pierce_p[2]) ** 2


def calculate_c_v(a, b, c, d):
	if c != 0:
		return array([0, 0, d / c])
	if b != 0:
		return array([0, d / b, 0])
	return array([d / a, 0, 0])


def calculate_s_t(a, b, c):
	if a != 0:
		return (
			array([b / a, 1, 0]),
			array([c / a, 0, 1])
		)
	if b != 0:
		return (
			array([1, a / b, 0]),
			array([0, c / b, 1])
		)
	return (
		array([1, 0, a / c]),
		array([0, 1, b / c])
	)


def calculate_distance_to_pierce_3(a, b, c, d, y, x):
	l_b = array([0, 0, -SHIFT_OF_OBSERVER])
	l_a = array([x, y, 0]) - l_b
	t = (d - a * l_b[0] - b * l_b[1] - c * l_b[2]) / (a * l_a[0] + b * l_a[1] + c * l_a[2])
	pierce_p = l_b + t * l_a
	return pierce_p[0] ** 2 + pierce_p[1] ** 2 + (SHIFT_OF_OBSERVER + pierce_p[2]) ** 2


calculate_distance_to_pierce_3(1, 0, 1, 10, 0, 0)
