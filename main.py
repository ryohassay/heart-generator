import turtle
import numpy as np


def draw_heart():
	for theta in np.linspace(0, 2 * np.pi, 500):
		x = 16 * np.sin(theta)
		y = 13 *np.cos(theta) - 5 * np.cos(2 * theta) - 2 * np.cos(3 * theta) - np.cos(theta)
		turtle.goto(x, y)


if __name__ == '__main__':
	draw_heart()
	turtle.done()
