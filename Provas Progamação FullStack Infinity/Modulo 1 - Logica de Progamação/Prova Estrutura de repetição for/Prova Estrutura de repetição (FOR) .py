numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))
soma = 0


for num in range(numero1, numero2 + 1):
    if num % 2 == 0:
        soma += num
if soma == 0:
    print('Não há numero pares no intervalo')
else:
    print(f'A soma total de numero pares foi de: {soma}')