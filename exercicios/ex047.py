#Fazer um programa que só mostre os números pares de 1 até 50

print('De um até 50, todos os números pares são:')
for c in range(0, 50, 2): #Dessa forma ele inclui o zero
    print(c, ", ", end='')

print('De um até 50, todos os números pares são:')
for c in range(1, 50): #Com o tratamento das estruturas de condições o programa fica perfeito
    if c % 2 == 0:
        print(c,", ", end='')

#Método Guanabara
for n in range(2, 51, 2):
    print(n, end=' ')
print('Acabou!')