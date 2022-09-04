# Reproduire un rectangle, un hexagone une sorte d'étoile (images disponible dans le vrais énoncé)

from turtle import *
begin_fill()

def rectangle():
	forward(100)
	left(90)
	forward(50)
	left(90)
	forward(100)
	left(90)
	forward(50)

def hexagone():
	for i in range(6):
		forward(100)
		left(60)

def etoile():
	for i in range(3):
		forward(100)
		backward(200)
		forward(100)
		left(60)

mainloop()
