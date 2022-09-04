# écrire un programme Turtle demandant à l'utilisateur un entier n et traçant un escalier à n marches.

from turtle import *

n = int(input("combien de marches? \n")
up()
goto(-200, -200)

down()
for i in range(n):
	left(90)
	forward(50)
	right(90)
	forward(50)

mainloop()
