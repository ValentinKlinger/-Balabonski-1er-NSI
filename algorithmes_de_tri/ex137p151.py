# faire un programme qui compare deux tableaux, supposés triés

def compare_tableaux(t, u):
    if len(t) != len(u):
        return False
    for i in range(len(t)):
        if t[i] != u[i]:
            return False
    return True
