# Ecrire un programme qui demande un entier n à l'utilisateur et affiche chacun l'une des figure suivante (dans un carré de côté n).

def figure_1(n):
    for i in range(1, n + 1):
        print(i * '#')


def figure_2(n):
    for i in range(n, 0, -1):
        print(i * '#')


def figure_3(n):
    for i in range(n, 0, -1):
        print((n - i) * '.' + i * '#')


def figure_4(n):
    print(n * '#')
    for _ in range(n - 2):
        print('#' + (n - 2) * '.' + '#')
    print(n * '#')

   

n = int(input('n ?\n'))
figure_1(n)
print('\n')
figure_2(n)
print('\n')
figure_3(n)
print('\n')
figure_4(n)

