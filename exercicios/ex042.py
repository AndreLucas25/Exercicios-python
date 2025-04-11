#Acrescentar o recurso de informar se o triangulo é escaleno, isósceles ou equilátero do ex035

#Meu método
print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima \033[31mPODEM FORMAR\033[m triângulo')
    if r1 == r2 == r3:
        print('O triângulo é \033[34mEquilátero\033[m. Todos os lados iguais.')
    elif r1 == r2 or r1 == r3 or r3 == r2:
        print('O triângulo é \033[34mIsósceles\033[m. Dois lados iguais.')
    else:
        print('O triângulo é \033[34mEscaleno\033[m. Todos os lados diferentes.')
else:
    print('Os segmentos acima NÃO PODEM FORMA triângulo')

#Método Guanabara
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima \033[31mPODEM FORMAR\033[m um triângulo', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 and r1 != r2:
        print('ESCALENO!')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMA triângulo')
