#Somar números impares de 1 a 500 e que sejam múltiplos de 3

s = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 != 0:
        s += c
print(f'O total da soma de números impares de 1 a 500 e múltiplos de 3 é {s}')

#Método Guanabara
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c, end=' ')
        cont += 1
        soma += c
print(f'A soma de todos os {cont} valores solicitados é {soma}')
