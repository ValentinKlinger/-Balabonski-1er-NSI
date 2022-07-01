# en sopposant que le temps de tri par selection est prend un temps proportionnel à N², et qu'il prend 6,8s pour triés 16000 valeurs
# déterminé le temps que ça prend de trié 1 000 000 valeurs avec un tris par selection

def temps_tris(n):
    return (n**2 * 6.8) / 16000 ** 2

if __name__ == '__main__':
    print(temps_tris(1000000))
