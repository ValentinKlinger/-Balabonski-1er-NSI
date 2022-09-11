# Ecrire une fonction echange(tab, i, j) qui échange dans le tableau tab les éléments d'indices i et j.

def echange(tab, i, j):
	tab[i], tab[j] = tab[j], tab[i]
	return tab
