#Ler dois números e perguntar qual operação o usuário quer realizar

op = 0 # variável que receberá a escolha do usuário
n_maior = 0 #Variável que receberá o maior valor
while op != 5: #O while vai continuar até o usuário escolher a opção 5
    n1 = float(input('Número 1: '))
    n2 = float(input('Número 2: '))
    print('''[1] \033[34mSomar\033[m 
[2]\033[34m multiplicar\033[m
[3] \033[34mMaior\033[m
[4] \033[34mNovos Números\033[m
[5] \033[34mSair do Programa\033[m''') #Menu para apresentação das opções para o usuário
    op = int(input('Opção: '))
    if op == 1: #Se a opção for 1, o programa vai somar
        print(f'{n1} + {n2} = {n1+n2}')
    elif op == 2: #Se a opção for 2, vai multiplicar
        print(f'{n1} x {n2} = {n1*n2}')
    elif op == 3: #Se for 3, vai mostrar o maior número digitado pelo usuário
        n_maior = n1
        if n2 > n_maior:
            n_maior = n2
        print(f'O maior número é {n_maior}')
    elif op == 4: #Se a opção for 4, ele vai digitar novos números
        print('Digite novamente!')
    elif op == 5: #Se a opção for 5
        print('Programa encerrado!')
    else: #Caso o usuário digite alguma opção inválida
        print('\033[31mErro! Digite uma opção válida!\033[m')

from time import sleep
#Método Guanabara
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''[ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('>>>>> Qual é a sua opção: '))
    if opção == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é {soma}')
    elif opção == 2:
        produto = n1 * n2
        print(f'A soma entre {n1} x {n2} é {produto}')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif opção == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')