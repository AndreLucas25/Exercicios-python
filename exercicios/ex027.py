#Ler o nome completo de uma pessoa e mostrar seu primeiro nome e o último

#Meu método
nm = str(input('Digite seu nome completo: ')).strip().title()
div = nm.split()
print(f'Seu nome completo é {nm}')
print(f'Seu primeiro nome é {div[0]}')
print(f'Seu ultimo nome é {div[-1]}')

#Método Guanabara
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu ultimo nome é {nome[len(nome)-1]}')