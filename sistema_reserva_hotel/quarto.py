# Define a classe quarto e seus tipos


class Quarto:
    def __init__(self, numero, tipo, capacidade, preco_por_dia):
        self.numero = numero  # numero do quarto
        self.tipo = tipo  # tipo de quarto (simples, suite)
        self.capacidade = capacidade  # capacidade maxima de hospedes
        self.status = "disponivel"
        self.preco_por_dia = preco_por_dia

    def verificar_disponibilidade(self):
        return self.status == "disponivel"

    def marcar_como_ocupado(self):
        self.status = "ocupado"

    def marcar_como_disponivel(self):
        self.status = "disponivel"

    def calcular_preco(self, total_dias):
        return self.preco_por_dia * total_dias

    def exibir_informacoes(self):
        print(f"Quarto {self.numero} - Tipo: {self.tipo}")
        print(f"Capacidade: {self.capacidade} pessoas ")
        print(f"Status: {self.status}")
        print(f"Preço por dia: R${self.preco_por_dia}")


class Simples(Quarto):
    def __init__(self, numero):
        super().__init__(numero, "simples", 2, 150)


class Suite(Quarto):
    def __init__(self, numero):
        super().__init__(numero, "suite", 4, 210)
