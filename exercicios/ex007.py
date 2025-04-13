#Média de um aluno

nome = str(input('Digite seu nome: ')) #Lê o nome do aluno
nota1 = float(input('Digite sua\033[34m primeira\033[m nota: ')) #Lê a primeira nota do aluno
nota2 = float(input('Digite sua\033[34m segunda\033[m nota: ')) #Lê a segunda nota do aluno
media = (nota1 + nota2) / 2 #Váriavel que vai receber a média entre as duas notas lidas
print(f'A média de \033[4m{nome}\033[m é \033[4m{media}\033[m') #Imprime o resultado da média entre as duas notas lidas