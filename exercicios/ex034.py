#Ler um sálario e calcular o valor do seu aumento

#Meu método
salario = float(input('Digite o seu sálario: R$'))
if salario > 1250:
    aumento = ((salario * 10) / 100) + salario
    print(f'O seu sálario era R${salario}, com o aumento de 10% ficou R${aumento:.2f}')
else:
    aumento = ((salario * 15) / 100) + salario
    print(f'O sálario era R${salario} com o aumento de 15% ficou R${aumento}')

#Método Guanabara
salário = float(input('Qual é o sálario do funcionário? R$'))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print(f'Quem ganhava R${salário:.2f} passa a ganhar R${novo:.2f} agora.')
