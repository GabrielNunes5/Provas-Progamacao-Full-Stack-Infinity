# criando a função
def maior_numero(a: float, b: float, c: float):
    # verificando qual é o maior dos 3 numeros
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


# chamando a função e passando os valores
maior = maior_numero(10, 180, 90)
print("O maior número é:", maior)