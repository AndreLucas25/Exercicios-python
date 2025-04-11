#Ler um número e informar se é par ou impa

#Meu método
numero = int(input('Digite um número: '))
if numero % 2 == 0:
    print(f'O número {numero} é par!')
else:
    print(f'O número {numero} é impa!')

#Método Guanabara
número = int(input('Me diga um número qualquer: '))
resultado = número % 2
if resultado == 0:
    print(f'O nÚmero {número} é PAR')
else:
    print(f'O número {número} é IMPAR')