#Fazer o computador pensar em um número inteiro, pedir para usuário tentar acertar e no fim uma mensagem informando se acertaram ou não
from random import randint
from time import sleep

#Minha solução
aleatorio = randint(0, 5)
print('Adivinhe o número que o computador está pensando:')
numero = int(input('Escolha um número de 0 a 5: '))
print('Parabens, você acertou!' if numero == aleatorio else 'Não foi dessa vez, '
          'tente novamente em uma próxima.' f' O número escolhido foi {aleatorio}')

#Método Guanabara
computador = randint(0, 5) #Faz o computador "pensar"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 50. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) #Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARÁBENS! Voceê conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no {jogador}!')