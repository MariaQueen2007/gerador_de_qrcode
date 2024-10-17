from random import randrange
lista_inteiros = []
qntd_numeros = 10
while qntd_numeros > 0:
    lista_inteiros.append(randrange(0, 60, 1))
    qntd_numeros =- 1

lista_inteiros.sort()
print(lista_inteiros)