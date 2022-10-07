# Donner une chaîne de documentation à la fonction division_euclidienne de la page 135.

def divison_euclidienne(a, b):
    '''Renvoie et quotient et le reste de la division de a par b.
    a doit être positif ou nul et b strictement possitif'''
    q = 0
    r = a
    while r >= b:
        q += 1
        r -= b
    return q, r
