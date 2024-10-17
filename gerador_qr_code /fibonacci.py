def fibo(atual, anterior, parada):
    if parada == 0:
        return
    novo_numero = atual + anterior
    print(novo_numero)
    parada -= 1
    fibo(novo_numero, atual, parada)
