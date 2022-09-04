# écrire un programme traçant une route en perspective.

from turtle import *

up()
goto(0, -200)
down()
for i in range(10, 0, -1):
	width(i)
	goto(xcor(), ycor() + 40)
up()

goto(-160, -200)
down()
for i in range(10, 0, -1):
	width(i)
	goto(xcor() + 15, ycor() + 40)
up()

goto(160, -200)
down()
for i in range(10, 0, -1):
	width(i)
	goto(xcor() - 15, ycor() + 40)
mainloop()
