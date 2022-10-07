# Ecrire une fonction nb_de_tours(n) qui renvoie le plsu petit entier k tel que 2**k > n, 
# c'est-à-dire le nombre maximal de valeurs examinée par la recherche dichotomique dans un tableau de taille n.

def nb_de_tours(n):
    k = 0
    while n > 1:
        k += 1
        n // 2
    return k
