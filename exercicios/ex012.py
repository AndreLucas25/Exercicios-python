#Ler o valor de um produto e informar seu novo valor com o desconto

print('Digite o valor do produto:')
produto = float(input('R$'))
novo_valor = produto-(produto*5/100)
print(f'O antigo valor do produto era R${produto}, com os 5% de desconto seu novo valor é R${novo_valor}')