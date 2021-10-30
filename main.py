import turtle
import numpy as np
from time import sleep


def draw_heart():
	COEFF = 20

	turtle.pen(fillcolor='red', pencolor='red', pensize=7)

	turtle.penup()
	turtle.goto(0, COEFF * 5)
	turtle.pendown()

	turtle.begin_fill()

	for theta in np.linspace(0, 2 * np.pi, 500):
		x = COEFF * (16 * np.sin(theta) ** 3)
		y = COEFF * (13 *np.cos(theta) - 5 * np.cos(2 * theta) - 2 * np.cos(3 * theta) - np.cos(4 * theta))
		turtle.goto(x, y)
		# print(x, y)
	
	sleep(2)
	turtle.end_fill()

if __name__ == '__main__':
	draw_heart()
	turtle.done()
