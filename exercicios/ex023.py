#Ler um número até 9999 e mostras sua unidade, dezena, centena e milhar

#Meu método
#Como str
numero = str(input('Digite um número. De 0 até 9999: '))
print(f'Unidade: {numero[3]}')
print(f'Dezena: {numero[2]}')
print(f'Centena: {numero[1]}')
print(f'Milhar: {numero[0]}')
#Se o número tiver menos que 4 dígitos, dá erro no programa. Então apesar de funcionar, não é um programa responsivo

#Método Guanabara
num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o numero {num}')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
#Esse apesar de ter mais código, é responsivo, não está sujeito a erros.