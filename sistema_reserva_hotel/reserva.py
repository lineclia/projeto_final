# define a classe reserva e suas funcionalidades

class Reserva:
    def __init__(self, quarto, cliente, data_entrada, data_saida):
        self.quarto = quarto
        self.cliente = cliente
        self.data_entrada = data_entrada
        self.data_saida = data_saida
        self.total_dias = (data_saida - data_entrada).days

    def exibir_informacoes(self):
        print(f"Quarto: {self.quarto.numero} - Tipo: {self.quarto.tipo}")
        print(f"Cliente: {self.cliente.nome}")
        print(f"Data de entrada: {self.data_entrada}")
        print(f"Data de saida: {self.data_saida}")
    
    def armazenar_reserva(self, reserva):
        self.reservas.append(reserva)