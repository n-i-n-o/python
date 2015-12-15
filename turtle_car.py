import turtle

""" Draws a car from loop_and_a_half file """

class GoTo:

	def __init__(self, x, y, width=1, color="black"):
		self.x = x
		self.y = y
		self.color = color
		self.width = width
	
	def draw(self, turtle):
		turtle.width(self.width)
		turtle.pencolor(self.color)
		turtle.goto(self.x, self.y)

class Circle:

	def __init__(self, radius, width=1, color="black"):
		self.radius = radius
		self.width = width
		self.color = color
	
	def draw(self, turtle):
		turtle.width(self.width)
		turtle.pencolor(self.color)
		turtle.circle(self.radius)

class BeginFill:

	def __init__(self, color="black"):
		self.color = color
	
	def draw(self, turtle):
		turtle.fillcolor(self.color)
		turtle.begin_fill()

class EndFill:
	
	def __init__(self):
		""" pass is simple a placeholder → nothing to initialize here all we 
		want is polymorphic behavior of draw method"""
		pass
	def draw(self, turtle):
		turtle.end_fill()

class PenUp:

	def __init__(self):
		pass
	def draw(self, turtle):
		turtle.penup()

class PenDown:

	def __init__(self):
		pass
	def draw(self, turtle):
		turtle.pendown()


class PyList:
	
	def __init__(self):
		self.items = []
	def append(self, item):
		self.items = self.items + [item]
	def __iter__(self):
		for c in self.items:
			yield c

def main():

	t = turtle.Turtle()
	screen = t.getscreen()
	file = open("loop_and_a_half", "r")

	# creating PyList to store graphics commands being read 
	graphicsCommands = PyList()

	command = file.readline().strip()
	while command != "":
		
		if command == "goto":
			x = float(file.readline())
			y = float(file.readline())
			width = float(file.readline())
			color = file.readline().strip()
			cmd = GoTo(x, y, width, color)
		elif command == "circle":
			radius = float(file.readline())
			width = float(file.readline())
			color = file.readline().strip()
			cmd = Circle(radius, width, color)
		elif command == "beginfill":
			color = file.readline().strip()
			cmd = BeginFill(color)
		elif command == "endfill":
			cmd = EndFill()
		elif command == "penup":
			cmd = PenUp()
		elif command == "pendown":
			cmd = PenDown()
		else:
			raise RuntimeError("What is {} supposed to mean?".format(command))

		graphicsCommands.append(cmd)

		command = file.readline().strip()
	
	# this iterates through the commands and does the drawing, making
	# use of __iter__ method
	for cmd in graphicsCommands:
		cmd.draw(t)


if __name__ == "__main__":
	print("[*] Initializing drawing ......")
	main()



