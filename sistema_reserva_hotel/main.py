# Definindo um quarto e o hotel
from cliente import Cliente
from quarto import Quarto, Simples, Suite, SuiteFamilia
from hotel import Hotel
from sistemacliente import SistemaCliente
from reserva import Reserva
from datetime import datetime

sistema_cliente = SistemaCliente()
hotel = Hotel("Hotel XYZ", "Rua 123, Cidade ABC")


#criando quartos
#quarto1 = Quarto(101, "simples", 2, 150)
#quarto2 = Quarto(102, "suite", 4, 250)

# Criando hotel
#hotel = Hotel("Hotel XYZ", "Rua 123, Cidade ABC")

# Armazenando os quartos no hotel
#hotel.armazenar_quarto(quarto1)
#hotel.armazenar_quarto(quarto2)

# listando os quartos do hotel
"""#hotel.listar_quartos_disponiveis()

# alterando status do quarto e verificando sua disponibilidade
quarto1.marcar_como_ocupado()
print(
    f"Quarto {quarto1.numero} disponível?\nO quarto está {'Disponível' if quarto1.verificar_disponibilidade() else 'Ocupado'}"
)


# listando os novos quartos disponiveis
#hotel.listar_quartos_disponiveis()"""
def inicializar_quartos():
    # Criando quartos pré-cadastrados
    quarto1 = Simples(101)
    quarto2 = Suite(102)
    quarto3 = SuiteFamilia(103)

    # Adicionando os quartos ao hotel
    hotel.armazenar_quarto(quarto1)
    hotel.armazenar_quarto(quarto2)
    hotel.armazenar_quarto(quarto3)

# Inicializa os quartos ao iniciar o programa
inicializar_quartos()
def menu():
    print("\n----- Sistema de Reservas de Quarto -----")
    print("1. Cadastrar Cliente")
    print("2. Fazer Reserva")
    print("3. Listar Quartos Disponíveis")
    print("4. Listar Reservas")
    print("5. Exibir Histórico de Clientes")
    print("0. Sair")

def cadastrar_cliente():
    print("\n----- Cadastrar Cliente -----")
    nome = input("Digite o nome do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    email = input("Digite o e-mail do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    cliente = Cliente(nome, telefone, email, cpf)
    print("Cliente cadastrado com sucesso!")

def fazer_reserva():
    print("\n----- Fazer Reserva -----")
    quarto_numero = int(input("Digite o número do quarto: "))
    cliente_cpf = input("Digite o CPF do cliente: ")
    data_entrada = input("Digite a data de entrada (dd/mm/aaaa): ")
    data_saida = input("Digite a data de saída (dd/mm/aaaa): ")
    
    quarto = hotel.obter_quarto_por_numero(quarto_numero)
    cliente = Cliente.obter_cliente_por_cpf(cliente_cpf)
    
    if quarto is None:
        print("Quarto não encontrado.")
        return
    
    if cliente is None:
        print("Cliente não encontrado.")
        return
    
    reserva = Reserva(
        quarto, 
        cliente, 
        datetime.strptime(data_entrada, "%d/%m/%Y"), 
        datetime.strptime(data_saida, "%d/%m/%Y")
    )

    """total_dias = (data_saida - data_entrada).days
    preco_total = quarto.get_preco_por_dia() * total_dias
    print(f"Valor total da reserva: R${preco_total:.2f}")"""

    quarto.marcar_como_ocupado()
    hotel.armazenar_reserva(reserva)
    print("Reserva realizada com sucesso!")

def listar_reservas():
    print("\n----- Lista de Reservas -----")
    reservas = hotel.obter_reservas()
    if not reservas:
        print("Nenhuma reserva registrada.")
    for reserva in reservas:
        reserva.exibir_informacoes()
        print("-" * 30)

def listar_quartos_disponiveis():
    hotel.listar_quartos_disponiveis()

def exibir_historico_clientes():
    SistemaCliente.exibir_historico_clientes()

while True:
    menu()
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        cadastrar_cliente()
    elif opcao == "2":
        fazer_reserva()
    elif opcao == "3":
        listar_quartos_disponiveis()
    elif opcao == "4":
        listar_reservas()
    elif opcao == "5":
        exibir_historico_clientes()
    elif opcao == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")