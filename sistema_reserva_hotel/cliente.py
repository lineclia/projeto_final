# Define a classe cliente e informações do hóspede
# Dados de cliente como privados

class Cliente:

    __historico_clientes = []

    def __init__(self, nome, telefone, email, cpf):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email
        self.__cpf = cpf
        
        Cliente.__historico_clientes.append(self)
    
    def exibir_informacoes(self):
        print(f"Nome: {self.__nome}")
        print(f"Telefone: {self.__telefone}")
        print(f"E-mail: {self.__email}")
        print(f"CPF: {self.__cpf}")
    
    def armazenar_cliente(self):
        return [self.__nome, self.__telefone, self.__email, self.__cpf]
    
    @classmethod
    def obter_historico_clientes(cls):
        return cls.__historico_clientes