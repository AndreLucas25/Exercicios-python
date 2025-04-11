#Jogar par ou impa com a máquina, o programa só será interrompido quando eu perder
from random import randint

print('-=' * 30) #Enfeite
print('VAMOS JOGAR PAR OU ÍMPAR') #Enfeite
print('-=' * 30) #Enfeite

cont = 0 #Varivel para contar
while True:
    valor = int(input('Diga um valor: ')) #Lendo o valor do usuário
    resp = str(input('Par ou Ímpar? ')).strip().upper()[0] #Lendo se o usuário escolhe par ou ímpar
    print('_' * 30) #Enfeite
    computador = randint(0, 10) #Sorteando de 0 a 10 o valor do jogador
    if resp == 'P': #Se o jogador escolher par
        soma = valor + computador #Realizando a soma do valor do jogador e computador
        if soma % 2 == 0: #Se o resto da divisão da soma for igual a 0 o jogador vence
            print(f'Você Jogou {valor} e o computador {computador}. Total de {soma} DEU PAR') #saida de dados
        else: #Se o resto da divisão for diferente de zero o jogador perde
            print(f'Você Jogou {valor} e o computador {computador}. Total de {soma} DEU IMPAR') #saida de dados
            print('Você perdeu!') #saida de dados
            print('-=' * 30) #Enfeite
            break #Encerrra o while
    if resp == 'I': #Se o jogador escolher ímpar
        soma = valor + computador #Realizando a soma do valor do jogador e computador
        if soma % 2 != 0: #Se o resto da divisão da soma for diferente de 0 o jogador vence
            print(f'Você Jogou {valor} e o computador {computador}. Total de {soma} DEU ÍMPAR')
        else: #Se o resto da divisão da soma for igual a 0 o jogador perde
            print(f'Você Jogou {valor} e o computador {computador}. Total de {soma} DEU PAR') #Saida de dados
            print('Você perdeu!') #Saida de dados
            print('-=' * 30) #Enfeite
            break #Encerrando o while
    cont += 1 #Toda vez que o programa chegar até aqui, é porque o jogador ganhou, ai o contador recebe +1
    print('_' * 30) #Enfeite
    print('Você VENCEU!') #saida de dados
    print('Vamos jogar novamente...') #Saida de dados
    print('-=' * 30) #Enfeite
print(f'\033[31mGAME OVER\033[m! Você Venceu {cont} vezes!') #Saida de dados
