#Ler o salário de um funcionário e informar como ficara após 15% de desconto

print('Digite seu salário:')
salario = float(input('R$'))
print(f'O antigo valor do seu salário era R${salario}, com os 15% de aumento fica R${salario+(salario*15/100)}')