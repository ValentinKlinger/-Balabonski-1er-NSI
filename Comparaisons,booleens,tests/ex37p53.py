# Ecrire un programme qui demande un entier n et qui affiche tous ses diviseurs
n = int(input('Que vaut n?\n'))
result = []

for number in range(1, (n // 2) + 1):
	print(number)
	if n % number == 0:
		result.append(number)

print(result)
