#Ler o nome, sexo e idade de 4 pessoas. No final mostrar a média de idade, o nome do homem mais velho e quantas mulheres tem mais de 20 anos

i_soma = 0 #Vai receber a soma das idades
maior = 0 #Vai receber a idade do homem mais velho
s = 0 #vai receber a quantidade total de mulheres acima de 20 anos
for c in range(0,4):
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: [M/F]')).strip().upper()
    i_soma += idade #somando as idades
    if idade > maior and sexo == 'M':
        maior = idade
        n = nome #Recebe o nome do homem mais velho
    if sexo[0] == 'F' and idade > 20:
        s += 1 #recebe a quantidade de mulheres acima dos 20 anos

print(f'A média de idade do grupo é {i_soma/4}') #Saida de dados
print(f'O nome do homem mais velho é {n}') #Saida de dados
print(f'A quantidade de mulheres acima de 20 anos é {s}') #Saida de dados

#Método Guanabara
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print(f'---- {p}ª PESSOA ----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade} anos')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos.')