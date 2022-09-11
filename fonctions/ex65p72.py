# Ecrire une fonction nbjourmoi(a, m) qui renvoie le nombre de jours dans un moi m d'une année a, utilisé le programme de l'ex 63
# pour les années bissextile.
import ex63p72

def nbjourmoi(a, m):
	if m in [1, 3, 5, 7, 8, 10, 12]:
		return 31
	elif m == 2:
		if ex63p72.bissextile(a):
			return 29
		else: 
			return 28
	else:
		return 30
