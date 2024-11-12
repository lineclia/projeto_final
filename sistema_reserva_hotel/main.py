# Definindo um quarto e o hotel
from quarto import Quarto
from hotel import Hotel

# criando quartos
quarto1 = Quarto(101, "simples", 2, 150)
quarto2 = Quarto(102, "suite", 4, 250)

# Criando hotel
hotel = Hotel("Hotel XYZ", "Rua 123, Cidade ABC")

# Armazenando os quartos no hotel
hotel.armazenar_quarto(quarto1)
hotel.armazenar_quarto(quarto2)

# listando os quartos do hotel
hotel.listar_quartos_disponiveis()

# alterando status do quarto e verificando sua disponibilidade
quarto1.marcar_como_ocupado()
print(
    f"Quarto {quarto1.numero} disponível?\nO quarto está {'Disponível' if quarto1.verificar_disponibilidade() else 'Ocupado'}"
)


# listando os novos quartos disponiveis
hotel.listar_quartos_disponiveis()
