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
