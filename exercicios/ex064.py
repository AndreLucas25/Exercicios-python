#ler números pelo teclado, somar, ver a quantidade de números digitados e só parar quando 999 foi digitado

n = 0 #Variavel que vai receber os valores do usuário
c = 0 #variavel que vai receber a quantidade de números digitados, exceto o flag
s = 0 #variavel que vai receber a soma dos números digitados, exceto o flag
while n != 999: #Estrutura de repetição, só irá parar quando digitarem 999
    n = int(input('Digite um número: (Digite 999 para parar) ')) #recebendo os valores dos usuário
    if n != 999: #Verificando se o número digitado é 999
        s += n #variavel recebendo os valores e somando
        c += 1 #variavel recebendo os valores e somando
print(f'Foram digitados {c} números.') #Saida de dados
print(f'A soma entre eles é igual à {s}') #saida de dados

#Método Guanabara
soma = cont = 0 #Variavel de contador e de soma
num = int(input('Digite um número [999 para parar}: ')) #Leitura dos números digitados pelo usuário
while num != 999: #Estrutura de repetição condicional. Enquanto o usuário não digitar 999, o programa continuará
    soma += num #Variavel somando os números digitados
    cont += 1 #Contando a quantidade de números digitados
    num = int(input('Digite um número [999 para parar}: ')) #Leitura dos números digitados pelo usuário
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.') #Saida de dados
