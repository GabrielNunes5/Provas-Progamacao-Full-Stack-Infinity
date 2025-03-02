class Quarto:
    def __init__(self, numero: int, tipo: str, preco_diaria: float):
        self.__numero = numero
        self.__tipo = tipo
        self.__preco_diaria = preco_diaria
        self.__disponivel = True

    @property
    def numero(self):
        return self.__numero

    @property
    def tipo(self):
        return self.__tipo

    @property
    def preco_diaria(self):
        return self.__preco_diaria

    @property
    def disponivel(self):
        return self.__disponivel

    @disponivel.setter
    def disponivel(self, status: bool):
        self.__disponivel = status

    def __str__(self):
        status = "Disponível" if self.__disponivel else "Ocupado"
        return f"Quarto {self.__numero} | {self.__tipo} | R${self.__preco_diaria} | {status}"
