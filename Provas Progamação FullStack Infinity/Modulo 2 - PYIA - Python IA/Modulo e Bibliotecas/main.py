from random import randint


def lancar_dados():
    dado1 = randint(1, 6)
    print(f'Primeiro dado: {dado1}')
    dado2 = randint(1, 6)
    print(f'Segundo dado: {dado2}')
    soma = dado1 + dado2
    return f'A soma dos dois dados é de: {soma}'


# Testando a função
print(lancar_dados())
