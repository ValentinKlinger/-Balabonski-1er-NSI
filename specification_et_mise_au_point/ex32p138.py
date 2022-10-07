# Donner un invariant de boucle pour la fonction suivante qui calcule x à la puissance n

def puissance(x, n):
    r = 1
    for i in range(n):
        r = r * x
        # invariant : r = x puissance i 
    return r
