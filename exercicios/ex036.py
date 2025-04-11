#Ler o valor da casa, o salário e quantos anos vai ser pago. Calcular o valor da prestação mensal e se exceder 30% do salário, ele não poderá comprar

#Meu método
nome = str(input('Qual o seu nome: '))
casa = float(input('Qual o valor da casa: R$'))
salario = float(input('Qual o valor do seu salário: R$'))
tempo = int(input('Quanto anos de pagamento: '))

prestacao = casa/(tempo*12)
exceder = salario*30/100

print(f'Bom dia, {nome}!')
if prestacao > exceder:
    print(f'Você não poderá comprar a casa. A prestação ficou no valor de R${prestacao:.2f}, valor ultrapassa os 30% do seu salário')
else:
    print(f'Você poderá comprar a casa! a prestação fica no valor de R${prestacao:.2f}')

#Método Guanabara
casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
minimo = salário * 30 / 1000
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos', end='')
print(f'A prestação será de R${prestação:.2f}')
if prestação <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')