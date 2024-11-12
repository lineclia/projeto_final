# Define a classe Sistema Cliente que irá armazenar os registros dos clientes

class SistemaCliente:
    def __init__(self):
        self.Cliente
    def exibir_historico_clientes(self):
        historico = cliente.obter_historico_clientes()
        for cliente in historico:
            cliente.exibir_informacoes()
            print("-" * 30)