class Pessoa:
    def __init__(self, nome: str, telefone: str, email: str):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor: str):
        if len(valor) < 3:
            raise ValueError("Nome deve ter pelo menos 3 caracteres")
        self.__nome = valor

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, valor: str):
        if not valor.isdigit() or len(valor) < 8:
            raise ValueError("Telefone inválido")
        self.__telefone = valor

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, valor: str):
        if "@" not in valor or "." not in valor:
            raise ValueError("E-mail inválido")
        self.__email = valor

    def exibir_informacoes(self):
        return f"{self.__nome} | {self.__telefone} | {self.__email}"
