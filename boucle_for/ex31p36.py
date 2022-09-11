# écrire un programme Turtle demandant à l'utilisateur un entier n et traçant un escalier à n marches.

import turtle

n = int(input("combien de marches? \n")
turtle.up()
turtle.goto(-200, -200)

turtle.down()
for i in range(n):
	turtle.left(90)
	turtle.forward(50)
	turtle.right(90)
	turtle.forward(50)

turtle.mainloop()
