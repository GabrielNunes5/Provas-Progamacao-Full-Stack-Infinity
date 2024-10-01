# criando a função
def media(a: float, b: float, c: float):
    media_aritimetica = (a+b+c)/3
    return media_aritimetica


# chamando a função e passando os valores
media_result = media(10, 20, 30)
print(f'O resultado é: {media_result}')