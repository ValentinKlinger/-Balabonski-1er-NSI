# Ecrire un programme tableau_croissant(n) qui r'envoie un tableau de taille n triés au hasard dont ayant la propriété d'être 
# trié par ordre croissant.
import random
def tableau_croissant(n):
	tableau = [random.randint(1, n + 100) for i in range(n)]
	tableau.sort()
	return tableau
