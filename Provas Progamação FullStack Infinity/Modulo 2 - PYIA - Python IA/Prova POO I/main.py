# Classe base Animal
class Animal:
    def falar(self):
        print("Este animal faz um som.")


# Subclasse Cachorro
class Cachorro(Animal):
    def falar(self):
        print("O cachorro late.")


# Subclasse Gato
class Gato(Animal):
    def falar(self):
        print("O gato mia.")


# Criando instâncias das classes
animal_generico = Animal()
cachorro = Cachorro()
gato = Gato()

# Testando cada metodo
animal_generico.falar()
cachorro.falar()
gato.falar()
