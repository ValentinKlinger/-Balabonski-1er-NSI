# Bin packing : programmation. ON veut écrire un programme qui étant donnés un
# tableau tab donnant les poids de chaques objet et un nombre n de conteneurs
# de capacité c, chercher à répartir l'ensemble des objets dans les conteneurs.
# Ecrire un programme qui indique s'il a réussi à répartir tous les objets
# en utilisant la première stratégie proposée à l'exercice 162.

def binpacking(tab, n, c):

    ncr = [[complice, 0] for complice in range(n)]

    for objet in tab:
        for complice in ncr:
            if complice[1] + objet <= c:
                complice[1] += objet
                break
            
            if complice[0] == ncr[-1][0]:
                return False
    return ncr
