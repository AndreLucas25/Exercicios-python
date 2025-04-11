#Fazer o programa que mostre a tabuada de vários números e só parar quando for digitado número negativo

while True: #Repetição infinita
    n = int(input('Quer ver a tabuada de qual valor? ')) #Lendo os números digitados
    if n < 0: #Se o número for menor que 0, o programa encerra
        break #Encerrando
    print('_'*20) #Enfeite
    for c in range(1, 11): #Repetição para tabuada
        print(f'{n} x {c} == {n*c}') #Saida de dados
    print('_' * 20) #enfeite
print('Programa Tabuada encerrado. \033[34mVolte Sempre!') #Saida de dados
