#Criar o jokenpô
import random
from time import sleep

from setuptools.build_meta import prepare_metadata_for_build_editable

#Meu método
print('\033[97mJOGO DE PEDRA PAPEL E TESOURA\033[m')
escolha = str(input('PEDRA, PAPEL OU TESOURA: ')).strip().upper()

a = "PEDRA"
b = "PAPEL"
c = "TESOURA"
computador = random.choice((a, b, c))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')

if escolha == 'PEDRA' and computador == 'TESOURA':
    print(f'Usuário Venceu! \033[34musuário\033[m escolheu \033[34m{escolha}\033[m e \033[31mcomputador\033[m escolheu \033[31m{computador}\033[m.')
elif escolha == 'PAPEL' and computador == 'PEDRA':
    print(f'Usuário Venceu! \033[34musuário\033[m escolheu \033[34m{escolha}\033[m e \033[31mcomputador\033[m escolheu \033[31m{computador}\033[m.')
elif escolha == 'TESOURA' and computador == 'PAPEL':
    print(f'Usuário Venceu! \033[34musuário\033[m escolheu \033[34m{escolha}\033[m e \033[31mcomputador\033[m escolheu \033[31m{computador}\033[m.')
elif escolha == computador:
    print(f'Empate! usuário escolheu {escolha} e computador escolheu {computador}.')
else:
    print(f'Computador Venceu! \033[31mcomputador\033[m escolheu \033[31m{computador}\033[m e \033[34musuário\033[m escolheu \033[34m{escolha}\033[m.')

#Método Guanabara
itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0,2)
jogador = int(input('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA'''))
print('-='*11)
print(f'O computador escolheu {itens[computador]}')
print(f'O jogador jogou {itens[jogador]}')
print('-='*11)
if computador == 0: #Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: #Computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: #computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')