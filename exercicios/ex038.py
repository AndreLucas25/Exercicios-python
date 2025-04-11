#Ler dois números inteiros e comparar, mostrando na tela o maior, o menor ou se forem iguais

#Meu método
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
if n1 != n2:
    if n1 > n2:
        maior = n1
        menor = n2
    elif n2 > n1:
        maior = n2
        menor = n1
    print(f'O maior é {maior} e o menor é {menor}')
else:
    print('Não existe valor maior, os dois são iguais.')

#Método Guanabara
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O PRIMEIRO valor é maior.')
elif n2 > n1:
    print('O SEGUNDO valor é maior.')
else:
    print('Os dois valores são IGUAIS.')
