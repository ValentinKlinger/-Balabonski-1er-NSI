# Reproduire un rectangle, un hexagone une sorte d'étoile (images disponible dans le vrais énoncé)

import turtle
begin_fill()

def rectangle():
	turtle.forward(100)
	turtle.left(90)
	turtle.forward(50)
	turtle.left(90)
	turtle.forward(100)
	turtle.left(90)
	turtle.forward(50)

def hexagone():
	for i in range(6):
		turtle.forward(100)
		turtle.left(60)

def etoile():
	for i in range(3):
		turtle.forward(100)
		turtle.backward(200)
		turtle.forward(100)
		turlte.left(60)

turtle.mainloop()
