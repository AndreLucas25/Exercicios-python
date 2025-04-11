#Ler três números e informar o maior e o menor

#Meu método
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais outro número: '))
if n1 > n2 > n3:
    print(f'O maior número é {n1} e o menor é {n3}')
else:
   print(f'O maior número é {max(n1, n2, n3)} e o menor é {min(n1, n2, n3)}')

#Método Guanabara
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
#Verificar o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificando o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')
