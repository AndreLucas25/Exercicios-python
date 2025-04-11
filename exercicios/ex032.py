#Ler um ano e informar se ele é bissexto
from datetime import date

#Meu método
ano = int(input('Digite um ano: '))
if ( ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('O ano é bissexto!')
else:
    print('O ano não é bissexto!')

#Método Guanabara
ano = int(input('Que ano quer analisar? coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} não é BISSEXTO')