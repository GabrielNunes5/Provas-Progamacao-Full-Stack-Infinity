from pessoa import Pessoa


class Cliente(Pessoa):
    ultimo_id = 0

    def __init__(self, nome: str, telefone: str, email: str):
        super().__init__(nome, telefone, email)
        Cliente.ultimo_id += 1
        self.__id = Cliente.ultimo_id

    @property
    def id(self):
        return self.__id

    def exibir_informacoes(self):
        base_info = super().exibir_informacoes()
        return f"ID {self.__id} | {base_info}"
