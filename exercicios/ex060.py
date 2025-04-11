#Ler um número e mostrar seu fatorial
from math import factorial


#Minhas soluções
#Resolução com while
'''n = int(input('Digite um número para saber seu fatorial: ')) #Número escolhido pelo usuário
c = n #a variável que servirá como multiplicador do número
f = n #variável que recebera a multiplicação e será multiplicador
print(f'{n} ', end='')
while c > 1: #enquanto a variável c for maior que 1, o while funcionará
    c -= 1 #A variável perdendo 1 a cada repetição do programa
    print(f'x {c} ', end='') #Saida do fatorial com formatação
    f = f * c #Calculo do fatorial
    if c == 1: #Verificando se o programa está em sua última repetição
        print('= ', end='') #Formatação do programa
print(f) #Saida de dados
print(f'O fatorial de {n} é {f}') #Saida de dados

#Resolução com for
numero = int(input('Digite um número: ')) #Lendo o número escolhido pelo usuário
f = numero #Variável f recebendo o valor da variável numero
print(f'{numero}!', end=' ')
print(numero, end=' ')
for c in range(numero-1, 0, -1): #Estrutura pra calcular o fatorial do número escolhido
    print('x', c,  end=' ') #saida de dados com formatação
    f = f * c #calculo
    if c == 1: #Se o laço estiver na última repetição, colocará o sinal de =
        print(f'= {f}') #Resultado final do fatorial
print(f'\nO fatorial de {numero} é {f}') #Saida de dados

#Método Guanabara
#Método math
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}')'''

n =int(input('Digite um número: '))
c = n
f = 1
print(f'Calculando {n}!', end=' ')
while c > 0:
    print(c, end=' ')
    print('x' if c > 1 else '=', end=' ')
    f *= c
    c -= 1
print(f'O fatorial de {n} é {f}')