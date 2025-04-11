#Média de um aluno

nome = str(input('Digite seu nome: '))
nota1 = float(input('Digite sua\033[34m primeira\033[m nota: '))
nota2 = float(input('Digite sua\033[34m segunda\033[m nota: '))
media = (nota1 + nota2) / 2
print(f'A média de \033[4m{nome}\033[m é \033[4m{media}\033[m')