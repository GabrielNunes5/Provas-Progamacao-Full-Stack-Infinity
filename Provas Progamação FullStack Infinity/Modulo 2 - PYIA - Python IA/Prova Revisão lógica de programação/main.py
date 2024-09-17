produtos = {}
contador = 0
valor_total = 0

while contador < 5:
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))

    produtos[nome] = preco
    valor_total += preco
    contador += 1


print(f'O valor total da compra foi de: {valor_total}')