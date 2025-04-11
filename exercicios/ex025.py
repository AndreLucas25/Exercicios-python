#Ler um nome e verificar se tem silva

#Meu método
nome = str(input('Digite seu nome: ')).strip().upper().title()
print(f'O nome {nome} tem silva? {"Silva" in nome}')

#Método Guanabara
nome = str(input('Qual o seu nome completo? ')).strip()
print(f'Seu nome tem Silva? {"silva" in nome.lower()}')