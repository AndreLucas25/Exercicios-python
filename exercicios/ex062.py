#Fazer o mesmo programa que o anterior, mas perguntar quantos termos o usuário quer

'''termo_1 = int(input('1º Termo: ')) #O 1º termo da p.a
r = int(input('Razão: ')) #A razão da p.a
n = 1 #Contador pra dar o limite ao while
while n != 11: #O while funcionara enquanto contador 'n' não for igual 11
    pa = termo_1 + (n -1) * r #Calculo para saber o valor do termo
    print(f'{n}º Termo é {pa}') #Saida dos termos da p.a
    n += 1 #Contador recebendo 1 até chegar ao limite de 11
    if n == 11: #Só vai executar os próximos comando caso o contador esteja em 11
        t = int(input('Quantos mais termos você quer ler: (digite 0 pra encerrar o programa) ')) #Vai perguntar se o usuário quer mais termos
        if t != 0: #Se o usuário digitar algo diferente de zero ele executa o programa abaixo
            for c in range(n, n+t): #ele vai começar por onze e vai até o último termo
                print(f'{c}º Termo é {pa+r}')  #Saida dos termos da p.a
                pa = pa + r #Recebendo a p.a anterior
                c += 1 #contador fazendo a contagem até chegar no limite'''

#Método Guanabara
print('Gerador de PA') #Titulo
print('-=' * 10) #Titulo
primeiro = int(input('Primeiro Termo: ')) #Lendo o primeiro termo da p.a
razão = int(input('Razão da PA: ')) #Lendo a razão da p.a
termo = primeiro #Uma variável recebendo o termo e que será mostrado na tela
cont = 1 #Contador responsável pelo limite do while
total = 0 #variável que será responsável por fazer comparação com o contador e permiti que o usuário escolha quantos mais termos quer ver
mais = 10 #Variável de limite inicial

while mais != 0: #Enquanto o usuário não digitar 0, o programa continuara
    total = total + mais #A variável de comparação com o contador recebendo o seu limite inicial do while
    while cont <= total: #Enquanto o a var cont for menor que a var total, ela mostrara 10 termos
        print(f'{termo} → ', end='') #Saida de dados com formatação
        termo += razão #a variável termo recebendo o valor da razão somado com o seu para mostrar o próximo termo
        cont += 1 #cont recebendo +1 até chegar no limite do programa
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? ')) #Lendo se o usuário quer mais termos
print(f'Progressão Finalizada com {total} termos mostrados.') #Saida de dados