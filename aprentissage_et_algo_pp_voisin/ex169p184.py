# Ecrire une fonction prenant en paramètres deux chaines c et d et indique si c peut être obtenue en retirant un caractère de d.

def d_devenir_c(c, d):
    ajout = 0
    
    try:
        for lettre in range(len(c)):
            if c[lettre] != d[lettre + ajout]:
                ajout += 1
                if c[lettre] != d[lettre + ajout]:
                    return False
    except IndexError:
        return False

    return (len(c) + ajout == len(d) or len(c) + ajout == len(d) - 1 + ajout) and ajout <= 1 
