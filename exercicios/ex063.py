#Ler um número e mostrar determinados números da sequência de fibonacci

n = int(input('Digite um número: ')) #Recebendo a quantidade de dígitos que o usuário quer no fibonacci

cont = 0 #Variavel que vai contar a quantidade de vezes que o programa se repete
a = 0 #variavel
b = 1 #variavel

while cont < n: #Enquanto o cont for menor que n o programa continuara
    print(a) #saida de dados
    a, b = b, a + b #atualizando os próximos valores da sequência
    cont += 1 #O contador recebendo +1 até seu limite

#Método Guanabara

print('='*30) #Enfeite
print('Sequência de Fibonacci') #Titulo
print('='*30) #Enfeite
n = int(input('Quantos termos você quer mostrar? ')) #Lendo quantos termos o usuário quer ver
t1 = 0 #primeiro termo padrão
t2 = 1 #Segundo termo padrão
print('~'*30) #Enfeite
print(f'{t1} → {t2}', end='') #saida de dados formatada
cont = 2 + 1 #Contador começando de 3, pois os dois primeiros termos é padrão
while cont <= n: #enquanto o contador for menor que os números de termos, o programa se repetirá
    t3 = t1 + t2 #O próximo termo é sempre a soma dos dois anteriores
    print(f' → {t3}', end=' ') #Saida de dados formatada
    t1 = t2 #O primeiro termo recebendo o segundo
    t2 = t3 #O segundo recebendo o terceiro
    cont += 1 #Contador recebendo +1 até chegar no limite
print('Fim') #Final do programa
