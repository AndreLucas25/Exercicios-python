#Refazer o exercício 9 utilizando o for

n = int(input('Digite um número inteiro: '))
print(f'A tabuada de {n}...')
for c in range(1, 11):
    print(f'{n} X {c:2} = {n*c}')

#Método Guanabara
num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print(f'{num} x {c:2} = {num*c}')