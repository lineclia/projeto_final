# Gerencia o hotel e sua lista de quartos e reservas


class Hotel:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.quarto = []
        # lista quarto para armazenar objetos Quarto

    def armazenar_quarto(self, quarto):
        self.quarto.append(quarto)
