# Ecrire un programme pour résoudre les équation de second degré.
import math
a = int(input('a\n'))
b = int(input('b\n'))
c = int(input('c\n'))

delta = (b ** 2) - 4 * a * c

if delta < 0:
    print("Il n'y a pas de solution")

elif delta == 0:
    print('La solution est :', - b / (2*a))

elif 0 < delta:
    print('les solutions sont :', (-b - math.sqrl(delta)) / (2 * a), 'et', (-b + math.sqrl(delta)) / (2 * a))
