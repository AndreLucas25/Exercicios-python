#Ler o 1° termo de uma p.a e no fim mostras seus 10 últimos termos

p_termo = int(input('Digite o 1° Termo da P.A: '))
r = int(input('Digite a razão da P.A: '))
for c in range(p_termo, p_termo + 10 * r, r): #Tive que fazer uma lógica para poder dar um parametro de parada
    print(c)
print('Fim!')

#Método Guanabara
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razão
for c in range(primeiro, decimo, razão):
    print(f'{c} ', end='→')
print('ACABOU')