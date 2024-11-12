# Gerencia o hotel e sua lista de quartos e reservas
class Hotel:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.quarto = []
        # lista quarto para armazenar objetos Quarto

    def armazenar_quarto(self, quarto):
        self.quarto.append(quarto)
        print(f"Quarto {quarto.numero} ({quarto.tipo})adicionado ao hotel {self.nome}.")

    def listar_quartos_disponiveis(self):
        print(f"Quartos disponíveis {self.nome}:")
        for quarto in self.quarto:
            if quarto.verificar_disponibilidade():
                print(f"Quarto {quarto.numero}: Disponível")
            else:
                print(f"Quarto {quarto.numero}: Ocupado")
