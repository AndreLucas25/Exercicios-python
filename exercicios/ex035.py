#Ler três segmentos de reta e informar se elas podem ou não formar um triangulo

#Meu método
r1 = int(input('Digite o segmento de uma reta: '))
r2 = int(input('Digite outro segmento de reta: '))
r3 = int(input('Digite mais um segmento de reta: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r3 + r2 > r1:
    print('Pode se formar um triângulo!')
else:
    print('Não pode se formar um triângulo!')

#Método Guanabara
print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo')
else:
    print('Os segmentos acima NÃO PODEM FORMA triângulo')