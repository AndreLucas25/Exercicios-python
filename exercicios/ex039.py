#Ler o ano de nascimento de um jovem e informar se ele pode ir ao exército, se não pode ou se já passou da hora
from datetime import date

#Meu método
nome = str(input('Digite Seu nome: ')).strip().title()
nascimento = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - nascimento

if idade > 18:
    print(f'Olá, {nome}! Já passou da hora de se alistar, se passaram {idade-18} anos.')
elif idade == 18:
    print(f'Olá, {nome}! Já está na hora de se alistar!')
elif idade < 18:
    print(f'Olá, {nome}! Ainda não chegou no momento do seu alistamento! Faltam {18-idade} anos.')

#Método Guanabara
sexo = str(input('Qual seu sexo? [M/F]')).title()
if sexo[0] == 'M':
    atual = date.today().year
    nasc = int(input('Ano de Nascimento: '))
    idade = atual - nasc
    print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')
    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        ano = atual + saldo
        print(f'Ainda faltam {saldo} anos para o alistamento.')
        print(f'Seu alistamento será em {ano}')
    elif idade > 18:
        saldo = idade - 18
        ano = atual - saldo
        print(f'Você já deveria ter se alistado há {saldo} anos.')
        print(f'Seu alistamento foi em {ano}')
elif sexo[0] == 'F':
    print('Você é mulher, não precisa se alistar!')