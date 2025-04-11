#Ler números e só parar quando for digitado o 999

c = s = 0 #Criando duas variáveis, uma para soma e outra para contar
while True: #Repetição infinita
    n = int(input('Digite um número (999 para parar): ')) #Lendo os números digitados pelo usuário
    if n == 999: #Se o número for 999, encerra a repetição
        break #Encerrando o while
    s += n #Somando os números digitados
    c += 1 #Contando a quantidade de repetições do programa
print(f'A soma dos {c} valores foi {s}!') #Saida de dados