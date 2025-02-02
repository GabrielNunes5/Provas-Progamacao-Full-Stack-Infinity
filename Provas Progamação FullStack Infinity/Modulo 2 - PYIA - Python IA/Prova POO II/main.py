# Classe base Veiculo
class Veiculo:
    def movimentar(self):
        print("Veículo está em movimento.")


# Subclasse Carro
class Carro(Veiculo):
    def movimentar(self):
        print("Carro está dirigindo.")


# Subclasse Moto
class Moto(Veiculo):
    def movimentar(self):
        print("Moto está acelerando.")


# Criando instâncias das classes
veiculo_generico = Veiculo()
carro = Carro()
moto = Moto()

# Testando cada metodo
veiculo_generico.movimentar()
carro.movimentar()
moto.movimentar()
