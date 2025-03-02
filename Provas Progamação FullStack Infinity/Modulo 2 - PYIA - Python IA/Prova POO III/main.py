class ContaBancaria:
    def __init__(self, titular, saldo=0.0):
        self._titular = titular  # Nome do titular da conta
        self._saldo = saldo  # Saldo inicial da conta

    # Adiciona um valor ao saldo da conta.
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    # Retira um valor do saldo da conta, se houver saldo suficiente.
    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

    # Exibe o saldo atual da conta.
    def exibir_saldo(self):
        print(f"Saldo atual: R${self._saldo:.2f}")


# Testando o codigo:
conta = ContaBancaria("João Silva", 1000.0)
conta.exibir_saldo()
conta.depositar(500.0)
conta.sacar(300.0)
conta.exibir_saldo()
