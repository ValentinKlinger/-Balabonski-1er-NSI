# Ecrire un programme qui construit un tableau de 100 entiers triés au hazard entre 1 et 1000, puis l'affiche.
import random 

tableau = [random.randint(1, 1000) for i in range(100)]

print(tableau)
