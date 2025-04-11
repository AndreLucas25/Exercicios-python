#Ler o sexo e idade, perguntar sempre se o usuário quer cadastrar mais pessoas

#Declarando variáveis
mulheres_menor_20 = 0 #variavel vai receber a quantidade de mulheres abaixo dos 20
cadastro_homens = 0 #Variavel para saber a quantidade de homens cadastrados
maior18 = 0 #Variavel para saber quantos têm mais de 18 anos
flag = '' #vai receber a resposta do usuário "S" ou "n"
sexo = '' #Vai receber o sexo do usuário

#Enfeites/Títulos
print('\033[33m') #Adicionando cores
print('_' * 30) #Enfeite
print('CADASTRE UMA PESSOA') #Enfeite
print('_' * 30) #Enfeite
print('\033[m') #Removendo cores

#While para cadastramento da idade e sexo
while True: #While infinito, até o usuário colocar que não quer continuar
    idade = int(input('Idade: ')) #Lendo a idade
    if idade > 18: #Analisando se a idade é maior de 18, se for a variável abaixo recebe +1
        maior18 += 1 #Recebendo +1
    sexo = str(input('Sexo: ')).strip().upper()[0] #Lendo o sexo
    if sexo != 'M' and sexo != 'F': #Se o sexo digitado for diferente de "M" e de "F", entrara em um looping até ele digitar corretamente
        while sexo != 'M' and sexo != 'F':  #Entrando no looping enquanto o sexo não for "M" ou "F"
            sexo = str(input('Sexo: ')).strip().upper()[0]  # Lendo o sexo
    if sexo == 'M': #se o sexo for masculino, a variável abaixo recebe +1
        cadastro_homens += 1 #Recebendo +1
    print('_' * 30)  # Enfeite
    if sexo == 'F' and idade < 20:
        mulheres_menor_20 += 1
    flag = str(input('Deseja continuar? ')).strip().upper()[0] #Lendo se o usuário quer ou não continuar
    if flag != 'S' and flag != 'N': #Se o flag for diferente de "S" e de "N", cai no looping, até o usuário digitar corretamente
        while flag != 'S' and flag != 'N':  # Entrando em looping enquanto não é "N" ou "N"
            flag = str(input('Deseja continuar? ')).strip().upper()[0]  # Lendo se o usuário quer ou não continuar
    if flag == 'S': #Se for igual a "S", o programa continua
        print('\033[33m')  # Adicionando cores
        print('_' * 30)  # Enfeite
        print('CADASTRE UMA PESSOA')  # Enfeite
        print('_' * 30)  # Enfeite
        print('\033[m')  # Removendo cores
    if flag == 'N': #Se for igual a "N", o programa encerra
        print('===== FIM DO PROGRAMA =====')
        break



#Saida de dados
print(f'Total de pessoas com mais de 18 anos: {maior18}.')
print(f'Ao todo temos {cadastro_homens} homens cadastrados.')
print(f'E temos {mulheres_menor_20} mulheres menos de 20 anos')