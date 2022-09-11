# ecrire une fonction bissextile(a) qui renvoie un booléen si une année est bissextile.

def bissextile(a):
	return a % 4 == 0 and (a % 100 != 0 or a % 400 == 0)
