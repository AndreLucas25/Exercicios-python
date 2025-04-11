#Ler um número e ver se ele é primo ou não

n = int(input('Digite um número: ')) #Número que será verificado
s = 0
for c in range(2, n): #O contador vai do número 2 até o número digitado pelo usuário.
    if n % c == 0 and c != n: #Aqui ele faz a verificação se o resto da divisão vai ser zero e se o número não está sendo dividido por ele mesmo.
        s += 1 #Caso o número seja divido por outro que não, seja ele mesmo, a variável vai receber um número.
if s == 0:
    print('O número é primo!') #Aqui irar sair o dado
else:
    print('O número não é primo') #Aqui irar sair o dado

#Método Guanabara
tot = 0
num = int(input('Digite um número: '))
for c in range(1,  num+1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')
print(f'\033[mO número {n} foi divisível {tot} vezes')
if tot == 2:
    print('E por isso ele é primo!')
else:
    print('E por isso ele nã é prim')