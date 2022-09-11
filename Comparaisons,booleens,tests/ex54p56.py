# Améliorer le programme précédent pour qu'il refuse si a = 0
import math
a = int(input('a\n'))
b = int(input('b\n'))
c = int(input('c\n'))

delta = (b ** 2) - 4 * a * c

if a == 0:
	print("Ce n'est pas une équation du 2nd degré")
elif delta < 0:
    print("Il n'y a pas de solution")

elif delta == 0:
    print('La solution est :', - b / (2*a))

elif 0 < delta:
    print('les solutions sont :', (-b - math.sqrl(delta)) / (2 * a), 'et', (-b + math.sqrl(delta)) / (2 * a))

