# Fait un drapeau français et d'un autre pays au choix avec turtle.

from turtle import * 

begin_fill()

def rectangle():
        forward(50)
        left(90)
        forward(100)
        left(90)
        forward(50)
        left(90)
        forward(100)

def france():
	up()
	fillcolor('blue')
	rectangle()
	end_fill()
	goto(xcor() + 50, ycor())
	left(90)
	begin_fill()
	fillcolor('white')
	rectangle()
	end_fill()
	goto(xcor() + 50, ycor())
	left(90)
	begin_fill()
	fillcolor('red')
	rectangle()
	end_fill()

def italie():
	up()
	fillcolor('green')
	rectangle()
	end_fill()
	goto(xcor() + 50, ycor())
	left(90)
	begin_fill()
	fillcolor('white')
	rectangle()
	end_fill()
	goto(xcor() + 50, ycor())
	left(90)
	begin_fill()
	fillcolor('red')
	rectangle()
	end_fill()

mainloop()
