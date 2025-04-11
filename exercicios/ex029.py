#Ler a velocidade de um carro na estrada, se ele passar 80km, mostrar uma mensagem de multa, e R$ 7,00 a cada km ultrapassado
from time import sleep

#Meu método
carro = int(input('Em quantos km você está? KM'))
if carro > 80:
    print('Você foi multado, passou os 80km!')
    multa = (carro - 80) * 7
    print('Analisando valor da multa.')
    sleep(2)
    print(f'O valor da multa é de R${multa:.2f}')

#Método Guanabara
velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    multa = (velocidade-80) * 7
    print(f'Você deve pagar uma multa de R${multa}:.2f}')
print('Tenha um bom dia! Dirija com segurança!')
