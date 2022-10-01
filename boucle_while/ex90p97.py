def nb_chifres(n):
    c = 1
    while n >= 10:
        n = n // 10
        c += 1
    return c
