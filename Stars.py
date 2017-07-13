import turtle
def star(n, k, size):
	turtle.resetscreen
	turtle.speed(n)
	angle = (k*360/n)
	for i in range(n):
		turtle.forward(size)
		turtle.right(angle)
	turtle.exitonclick()
def spiro(n, size):
	m = 1
	d = n
	turtle.resetscreen
	turtle.speed(10000)
	angle = 360/n
	for i in range(n):
		m = m+1
		d = d-1
		for j in range(36):
			turtle.forward(size/m)
			turtle.right(10)

		turtle.right(angle)
	turtle.exitonclick()
