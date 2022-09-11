# Programme qui demande des entiers et les renvoies dans l'ordre.
entiers = []

while True:
	new_number = input('Entrer un enter\n')
	if new_number == '':
		break
	entiers.append(int(new_number))

entiers.sort()
print(entiers)
