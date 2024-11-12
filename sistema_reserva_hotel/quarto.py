# Define a classe quarto e seus tipos


class Quarto:
    def __init__(self, numero, tipo, capacidade, preco_por_dia):
        self.__numero = numero  # numero do quarto
        self.__tipo = tipo  # tipo de quarto (simples, suite)
        self.__capacidade = capacidade  # capacidade maxima de hospedes
        self.__status = "disponivel"
        self.__preco_por_dia = preco_por_dia

    def get_numero(self):
        return self.__numero

    def set_numero(self, numero):
        self.__numero = numero

    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, tipo):
        self.__tipo = tipo

    def get_capacidade(self):
        return self.__capacidade

    def set_capacidade(self, capacidade):
        self.__capacidade = capacidade

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def verificar_disponibilidade(self):
        return self.__status == "disponivel"

    def marcar_como_ocupado(self):
        self.__status = "ocupado"

    def marcar_como_disponivel(self):
        self.__status = "disponivel"

    def calcular_preco(self, total_dias):
        return self.__preco_por_dia * total_dias

    def exibir_informacoes(self):
        print(f"Quarto {self.get_numero()} - Tipo: {self.get_tipo()}")
        print(f"Capacidade: {self.get_capacidade()} pessoas ")
        print(f"Status: {self.get_status()}")
        print(f"Preço por dia: R${self.__preco_por_dia}")


class Simples(Quarto):
    def __init__(self, numero):
        super().__init__(numero, "simples", 2, 180)


class Suite(Quarto):
    def __init__(self, numero):
        super().__init__(numero, "suite", 3, 210)


class SuiteFamilia(Quarto):
    def __init__(self, numero):
        super().__init__(numero, "suite", 4, 240)
