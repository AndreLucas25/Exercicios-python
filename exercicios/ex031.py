#Ler a distância de uma viagem em km e calcular o valor da passagem com base na distância
from time import sleep

#Meu método
distancia = int(input('Qual a distância da viagem? KM'))
if distancia <= 200:
    print('Avaliando valor da passagem!')
    sleep(2)
    passagem = distancia * 0.50
    print(f'O valor da passagem ficou R${passagem:.2f}')
else:
    print('Avaliando valor da passagem!')
    sleep(2)
    passagem = distancia * 0.45
    print(f'O valor da passagem ficou R${passagem:.2f}')

#Método Guanabara
distância = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {distância}km')
if distancia <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print(f'E o preço de sua passagem será de R${preço:.2f}')

#simplificado
distância = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {distância}km')
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print(f'E o preço de sua passagem será de R${preço:.2f}')