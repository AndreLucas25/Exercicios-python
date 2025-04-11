#Ler vários números inteiros pelo teclado, no final mostrar a média entre eles, o maior, o menor

s = 0 #Variavel que vai receber soma
c = 0 #variavel que vai receber a quantidade de números digitados
maior = 0 #variavel que vai receber o maior valor
menor = float('inf') #variavel que vai receber o menor valor
r = ' ' #Variavel que vai receber a resposta do usuário

while r[0] != 'N': #Enquanto o usuário não digitar "Não", o programa se repetirá
    n = int(input('Digite um número: ')) #Lendo os números digitados pelo usuário
    s += n #Somando os valores digitados
    c +=1 #Contando a quantidade de valores digitados
    if n > maior: #Verificando se é o maior número
        maior = n #Recebendo o maior número
    if n < menor: #Verificando se é o menor número
        menor = n #Recebendo o menor número
    r = str(input('Quer continuar: [S/N] ')).upper().strip()  # Perguntando se o usuário quer continuar
    while r[0] not in 'SN':
        print('\033[31mEscreva S ou R\033[m')
        r = str(input('Quer continuar: [S/N] ')).upper().strip()  # Perguntando se o usuário quer continuar

media = s / c #Calculando a média dos números
print(f'A Médias de todos os valores é {media}') #Saida de dados
print(f'O maior valor digitado foi {maior}') #Saida de dados
print(f'O menor valor digitado foi {menor}') #Saida de dados

#Método Guanabara
resp = 'S' #Variavel que será usada como condição no while
media = soma = quant = maior = menor = 0 #Variavel para somar, calcular média, quantidade de valores, maior e menor número
while resp in 'Ss': #Enquanto o usu ário digitar "s" o programa continua
    num = int(input('Digite um número: ')) #Lendo números digitados pelo usuário
    soma += num #Somando os valores digitados
    quant += 1  #Calculando a quantidade de vezes que o programa se repete
    if quant == 1: #Se for a primeira repetição, a variável maior e menor recebem o valor
        maior = menor = num #Recebendo o valor
    else: #Se não for a primeira repetição, maior re
        if num > maior: #Se o valor de num for maior do que o valor de maior, maior recebe num
            maior = num #maior recebendo num
        if num < menor: #Se o valor de num for menor que o valor de menor, menor recebe num
            menor = num #menor recebendo num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0] #Perguntando se o usuário quer continuar
media = soma / quant #Calculando a média dos valores digitados
print(f'Você digitou {quant} números e a média foi {media}') #Saida de dados
print(f'O maior valor foi {maior} e o menor foi {menor}') #Saida de dados
