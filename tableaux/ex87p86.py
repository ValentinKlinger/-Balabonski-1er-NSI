# Ecrire une fonction hamming(tab1, tab2) qui prend en paramètres deux tableaux que l'on supposera de la même taille
# et qui renvoie le nombre d'indices auxquels les deux tableaux diffèrent.

def hamming(tab1, tab2):
	diff_index = []
	for i in range(len(tab1)):
		if tab1[i] != tab2[i]:
			diff_index.append(i)
	return diff_index
