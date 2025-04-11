#Ler o 1º termo e a razão de uma p.a
from ex051 import primeiro

termo_1 = int(input('1º Termo: ')) #O 1º termo da p.a
r = int(input('Razão: ')) #A razão da p.a
n = 1 #Contador pra dar o limite ao while
while n < 11: #O while funcionara enquanto contador 'n' não for igual 11
    pa = termo_1 + (n -1) * r #Calculo para saber o valor do termo
    print(f'{n}º Termo é {pa}') #Saida dos termos da p.a
    n += 1 #Contador recebendo 1 até chegar ao limite de 11

#Método Guanabara
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} →', end='')
    termo += razão
    cont += 1
print('Fim!')
