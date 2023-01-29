# Ecrie une fonction calculant la distance de Hamming entre deux chaînes de
# caractères.

def hamming(chaine_1, chaine_2):

    dist = 0

    for lettre in range(min(len(chaine_1), len(chaine_2))):
        if chaine_1[lettre] != chaine_2[lettre]:
            dist += 1

    return dist + max(len(chaine_1), len(chaine_2)) - min(len(chaine_1), len(chaine_2))
