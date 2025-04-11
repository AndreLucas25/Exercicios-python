#ler o nascimento de um atleta e mostrar sua categoria
from datetime import date

#Meu método
nome = str(input('Digite seu nome: ')).title().strip()
nascimento = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - nascimento
print(idade)

if idade <= 9:
    print('Olá {nome}, sua categoria é \033[4mmirim\033[m')
elif 9 < idade <= 14:
    print(f'Olá {nome}, sua categoria é \033[4minfantil\033[m')
elif 14 < idade <= 19:
    print(f'Olá {nome}, sua categoria é \033[4mjunior\033[m')
elif 19 < idade <=20:
    print(f'Olá {nome}, sua categoria é \033[4msênior\033[m')
elif idade > 20:
    print(f'Olá {nome}, sua categoria é \033[4mmaster\033[m')

#Método Guanabara
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print(f'O atleta tem {idade} anos')
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
