# Dans la toute derniere étape du tris par selection (programme 14), il n'y a qu'une seul valeur dans la partie droite et il est donc innutile
# d'y chercher la plus petite valeur ni de l'échangé avec elle même. Modifier le programme 14 pour évité cette étape innutile.

# programme 14 (il tris une liste par ordre croissant):
'''
def echange(t, i, j):
    tmp = t[i]
    t[i] = t[j]
    t[j] = tmp

def trie_par_selection(t):
    for i in range(len(t)):
        m = i
        for j in range(i + 1,len(t)):
            if t[j] < t[m]:
                m = j
        echange(t, i, m)'''

# mon obtimisation :
def echange(t, i, j):
    tmp = t[i]
    t[i] = t[j]
    t[j] = tmp

def trie_par_selection(t):
    for i in range(len(t) - 1): # la modif est dans range(len(t)) qui devient range(len(t) - 1)
        m = i
        for j in range(i + 1,len(t)):
            if t[j] < t[m]:
                m = j
        echange(t, i, m)
