#Ler o nome de 4 alunos e sortear um dos nomes para apagar o quadro

from random import choice

a1 = input('Digite seu nome: ')
a2 = input('Digite seu nome: ')
a3 = input('Digite seu nome: ')
a4 = input('Digite seu nome: ')
sorteado = choice((a1, a2, a3, a4))
print(f'O aluno sorteado para apagar o quadro foi {sorteado}')

#Método Guanabara
n1 = str(input('Digite seu nome: '))
n2 = str(input('Digite seu nome: '))
n3 = str(input('Digite seu nome: '))
n4 = str(input('Digite seu nome: '))
lista = [n3, n4, n2, n1]
escolhido = choice(lista)
print(f'O aluno escolhido que irá pagar o quadro é {escolhido}')
