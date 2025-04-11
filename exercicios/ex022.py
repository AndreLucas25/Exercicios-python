#Ler um nome completo e mostrá-lo em maiúsculo, minúsculo, a quantidade de letra sem considerar os espaços e quantas letras tem o primeiro nome

#Meu método
nm = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome todo em maiúsculo {nm.upper()}') #maiúsculo

print(f'Seu nome todo em maiúsculo {nm.lower()}') #minúsculo

div = nm.split()
print(f'Quantidade de letras do nome {nm} é {len("".join(div))}') #Quantidade de letras

dividido = nm.split()
print(f'A quantidade de letras do primeiro nome é {len(dividido[0])}') #Quantidade de letra 1° nome

#Método Guanabara
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras') #len(nome) = A quantidade de letras = nome.count, quantidade de espaços
print(f'Seu primeiro nome tem {nome.find(" ")} letras')