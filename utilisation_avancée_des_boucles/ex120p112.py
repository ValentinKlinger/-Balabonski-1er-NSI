# Ecrire une fonction damier(n), qui prend en paramettre un entier n et trace avec turtle un damier de n case de côté
import turtle 


def carre(x, y, n):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    for _ in range(4):
        turtle.left(90)
        turtle.forward(n)

def carre_rempli(x, y, n):
    turtle.begin_fill()
    carre(x, y, n)
    turtle.end_fill()


def damier(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if (i + j) % 2 == 0:
                carre_rempli(20 * i, 20 * j, 20)
            else:
                carre(20 * i, 20 * j, 20)


turtle.exitonclick()
