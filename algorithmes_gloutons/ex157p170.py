# Ecrire un programme qui détermine une somme, en dessous de 2€, qui demande le 
# plus de pièces pour être rendue. Dit autrement, on recherche un entier s plus 
# petit que 200 qui maximise le résultat de monnaie(s).

max = 0
for centimes in range(200):
    if monnaie(centimes) > max:
        max = monnaie(centimes)

print(max)
