import os


def listar_diretorio():
    itens = os.listdir()
    print("Itens do diretório atual:")
    for item in itens:
        print(item)


listar_diretorio()
