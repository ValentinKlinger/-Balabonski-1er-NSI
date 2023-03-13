# Appliquer chacune des trois stratégies gloutones suivantes aux situations de l'exercice précédent.
# 1. Prendre à chaque fois l'objet le plus lourd que l'on peut.
# 2. Prendre à chaque fois l'objet moins lourd que l'on peut.
# 3. choisir les objets par ordre de rapport valeur/poids décroissant parmi ceux quine dépassent pas la capacité restante

def glouton_1(poids, valeurs):
    capacite = 10
    valeur_total = 0
    
    while min(poids) <= capacite:
        if max(poids) <= capacite:
            valeur_total += valeur[poids.index(max(poid))]
            capacite -= max(poids)
        poids.pop(poids.index(max(poids)))
        valeur.pop(poids.index(max(poid)))
    
    return valeur_total


def glouton_2(poids, valeurs):
    capacite = 10
    valeur_total = 0
    
    while min(poids) <= capacite:
        valeur_total += valeur[poids.index(min(poid))]
        capacite -= min(poids)
        poids.pop(poids.index(min(poids)))
        valeur.pop(poids.index(min(poid)))
    
    return valeur_total


def glouton_3(poids, valeurs):
    capacite = 10
    valeur_total = 0
    ratio = [i / poids[i] for i in valeurs]

    while min(poids) <= capacite:
        if poids[ratio.index(max(ratio))] <= capacite:
            valeur_total += valeurs[ratio.index(max(ratio))]
            capacite -= max(ratio)
        poids.pop(ratio.index(max(ratio)))
        valeurs.pop(ratio.index(max(ratio)))
        ratio.pop(ratio.index(max(ratio)))
    
    return valeur_total
