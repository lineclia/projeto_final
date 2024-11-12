# define a classe reserva e suas funcionalidades

class Reserva:
    def __init__(self, quarto, cliente, data_entrada, data_saida):
        self.quarto = quarto
        self.cliente = cliente
        self.data_entrada = data_entrada
        self.data_saida = data_saida
        self.total_dias = (data_saida - data_entrada).days

    def calcular_valor_total(self):
        # Multiplica o número de dias pela diária do quarto
        return self.quarto.calcular_preco(self.total_dias)
    
    def exibir_informacoes(self):
        print(f"Quarto: {self.quarto.get_numero()} - Tipo: {self.quarto.get_tipo()}")
        print(f"  Nome: {self.cliente._Cliente__nome}")
        print(f"  Telefone: {self.cliente._Cliente__telefone}")
        print(f"  E-mail: {self.cliente._Cliente__email}")
        print(f"  CPF: {self.cliente._Cliente__cpf}")
        print(f"Data de entrada: {self.data_entrada.strftime('%d/%m/%Y')}")
        print(f"Data de saída: {self.data_saida.strftime('%d/%m/%Y')}")
        print(f"Valor total da reserva: R$ {self.calcular_valor_total():.2f}")
