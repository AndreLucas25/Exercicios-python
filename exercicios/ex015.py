#Aluguel de carros

dias = int(input('Dias alugados: '))
Km = float(input('KM rodados: '))
valor = (dias * 60) + (Km * 0.15)
print(f'O Total a pagar é de R${valor:.2f}')