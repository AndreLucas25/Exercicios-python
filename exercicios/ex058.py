#Melhorar o jogo, permitindo o jogador continuar até acertar e mostrando quantos palpites ele deu
from random import randint

from ex028 import jogador

numero = float() #Varivel criada com valor infinito
aleatorio = randint(0, 10) #Gerando valores aleatórios para o programa
c = 0 #Variável que será contador
print('Adivinhe o número que o computador está pensando:')

while numero != aleatorio: #A condição de se o jogador não acertar, o programa continua
    c = c + 1 #contando a quantidade de vezes que o programa se repete, para saber quantos palpites o jogador deu
    numero = int(input('Escolha um número de 0 a 10: ')) #Perguntando o palpite do jogador
    print('Parabens, você acertou!' if numero == aleatorio else '\033[31mNão foi dessa vez, '
                  'tente novamente!\033[m') #Condição para saber se o jogador acertou.
print(f'O número pensado pelo programa foi {aleatorio} e a quantidade de palpites do jogador foi {c}') #Saida dos dados

#Método Guanabara
computador = randint(0, 10) #Faz o computador "pensar"
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        else:
            print('Menos... Tente mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns!')