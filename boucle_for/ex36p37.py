# écrire un programme turtle qui demande un entier n à l'utilisateur et trace une spirale de Fibonacci effectuant n/4 tours.

from turtle import *

n = int(input('quel est la valeur de n? \n'))

fib_a, fib_b = 0, 1

for i in range(1, n):
	circle(fib_b, 90)
	fib_a, fib_b = fib_b, fib_a + fib_b

mainloop()
