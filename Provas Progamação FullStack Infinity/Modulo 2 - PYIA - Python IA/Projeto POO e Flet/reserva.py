from datetime import datetime


class Reserva:
    def __init__(self, cliente, quarto, check_in: datetime, check_out: datetime):
        self.cliente = cliente
        self.quarto = quarto
        self.check_in = check_in
        self.check_out = check_out
        self.status = "Ativa"

    def calcular_valor_total(self):
        dias = (self.check_out - self.check_in).days
        return dias * self.quarto.preco_diaria

    def __str__(self):
        return (f"Reserva {self.status} - Quarto {self.quarto.numero}\n"
                f"Cliente: {self.cliente.nome}\n"
                f"Período: {self.check_in.strftime('%d/%m/%Y')} a {self.check_out.strftime('%d/%m/%Y')}")
