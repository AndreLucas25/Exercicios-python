#Ver o valor que o usuário tem na carteira e ver quantos dólares ele pode comprar

print('\033[35mDigite o valor que você tem na carteira\033[m:')
real = float(input('\033[35mR$\033[m'))
dolar = real / 6.10
print(f'Com R${real} você pode comprar US${dolar:.2f}')
