# écrire un programme traçant une route en perspective.

import turtle

turtle.up()
turtle.goto(0, -200)
turtle.down()
for i in range(10, 0, -1):
	turtle.width(i)
	turtle.goto(xcor(), ycor() + 40)
turtle.up()

turtle.goto(-160, -200)
turtle.down()
for i in range(10, 0, -1):
	turtle.width(i)
	turtle.goto(xcor() + 15, ycor() + 40)
turtle.up()

turtle.goto(160, -200)
turtle.down()
for i in range(10, 0, -1):
	turtle.width(i)
	turtle.goto(xcor() - 15, ycor() + 40)
turtle.mainloop()
