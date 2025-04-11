#Ler o peso de 5 pessoas e no final mostrar o maior e menor

maior = 0
menor = float('inf')
for c in range(1, 6):
    peso = float(input('PESO: KG='))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'O maior peso é de KG{maior}')
print(f'O menor peso é de KG{menor}')

#Método Guanabara
maior = 0
menor = 0
for p in range(1, 6):
    peso =  float(input('Peso da {}ª pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}kg')
print(f'O menor peso lido é de {menor}kg')