#Ler o sexo de uma pessoa, mas só aceitar 'M' ou 'F'

sexo = '' #Criação da variável sexo
while sexo != 'M' and sexo != 'F': #Se o sexo for diferente de umas dessas duas letras, o programa continua
    sexo = str(input('Digite seu sexo: [M/F] ')).upper() #Aqui ele pede o sexo, se receber algo diferente de F ou M, dára erro
    if sexo != 'M' and sexo != 'F':
        print('\033[31mTente novamente. Digite sexo válido\033[m')

#Método Guanabara
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')