#Escrever um programa que leia um número inteiro qualquer e peça para o usuário escolher a base de conversão

#Meu Método
print('\033[33mCONVERSÃO DE NÚMEROS\033[m')
num = int(input('Digite um número: '))
base = int(input('1 PARA binário \n'
                 '2 PARA octal \n'
                 '3 PARA hexadecimal: '))

if base == 1:
    conversor = bin(num)[2:]
    print(f'O número {num} em binário é {conversor}')
elif base == 2:
    conversor = oct(num)[2:]
    print(f'O número {num} em octal é {conversor}')
else:
    conversor = hex(num)
    print(f'O número {num} em hexadecimal é {conversor}')

#Uma melhor formatação
if base == 1:
    print(f'O número {num} em binário é {num:b}')
elif base == 2:
    print(f'O número {num} em octal é {num:o}')
else:
    print(f'O número {num} em hexadecimal é {num:x}')

#Método Guanabara
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif opção == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif opção == 3:
    print(f'{num} convertido para HEXADÉCIMAL é igual a {hex(num)[2:]}')
else:
    print('Opção inválida. Tente novamente.')