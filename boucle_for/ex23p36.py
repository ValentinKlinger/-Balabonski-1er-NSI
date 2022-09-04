# écrire un programme qui calcule et affiche 1 x 2 x ... x 100.

result = 1

for i in range(1, 101):
	result = result * i
	print(i)

print('Le résultat est :', result)
