from reserva import Reserva


class GerenciadorReservas:
    def __init__(self):
        self.__reservas = []
        self.__clientes = []
        self.__quartos = []

    def adicionar_quarto(self, quarto):
        self.__quartos.append(quarto)

    def registrar_cliente(self, cliente):
        self.__clientes.append(cliente)

    def verificar_disponibilidade(self, quarto, check_in, check_out):
        if not quarto.disponivel:
            return False

        for reserva in self.__reservas:
            if reserva.quarto == quarto:
                if (check_in < reserva.check_out) and (check_out > reserva.check_in):
                    return False
        return True

    def criar_reserva(self, cliente, quarto, check_in, check_out):
        if self.verificar_disponibilidade(quarto, check_in, check_out):
            reserva = Reserva(cliente, quarto, check_in, check_out)
            quarto.disponivel = False
            self.__reservas.append(reserva)
            return reserva
        return None

    def cancelar_reserva(self, reserva):
        reserva.status = "Cancelada"
        reserva.quarto.disponivel = True
        self.__reservas.remove(reserva)

    @property
    def reservas(self):
        return self.__reservas.copy()

    @property
    def clientes(self):
        return self.__clientes.copy()

    @property
    def quartos(self):
        return self.__quartos.copy()
