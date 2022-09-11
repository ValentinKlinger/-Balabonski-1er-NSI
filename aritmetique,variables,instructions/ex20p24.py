# Fait un drapeau français et d'un autre pays au choix avec turtle.

import turtle 

turtle.begin_fill()

def rectangle():
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(100)

def france():
	turtle.up()
	turtle.fillcolor('blue')
	turtle.rectangle()
	turtle.end_fill()
	turtle.goto(xcor() + 50, ycor())
	turtle.left(90)
	turtle.begin_fill()
	turtle.fillcolor('white')
	turtle.rectangle()
	turtle.end_fill()
	turtle.goto(xcor() + 50, ycor())
	turtle.left(90)
	turtle.begin_fill()
	turtle.fillcolor('red')
	turtle.rectangle()
	turtle.end_fill()

def italie():
	turtle.up()
	turtle.fillcolor('green')
	turtle.rectangle()
	turtle.end_fill()
	turtle.goto(xcor() + 50, ycor())
	turtle.left(90)
	turtle.begin_fill()
	turtle.fillcolor('white')
	turtle.rectangle()
	turtle.end_fill()
	turtle.goto(xcor() + 50, ycor())
	turtle.left(90)
	turtle.begin_fill()
	turtle.fillcolor('red')
	turtle.rectangle()
	turtle.end_fill()

turtle.mainloop()
