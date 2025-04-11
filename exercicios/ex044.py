#Ler o valor de um produto, e ajustar o valor conforme a forma de pagamento

#Meu método
preço = float(input('Preço das compras: R$'))
pagamento = int(input('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
Qual é a opção? '''))

if pagamento == 1:
    desconto = preço - (preço * 10 / 100)
    print(f'Sua compra de R${preço:.2f} vai custar R${desconto:.2f} no final.')
elif pagamento == 2:
    desconto = preço - (preço * 5 / 100)
    print(f'Sua compra de R${preço:.2f} vai custar R${desconto:.2f} no final.')
elif pagamento == 3:
    print(f'Sua compra continua custando R${preço:.2f}')
elif pagamento == 4:
    parcelas = int(input('Quantas parcelas? '))
    if parcelas <= 2:
        print(f'Sua compra continua custando R${preço:.2f}')
    else:
        juros = preço + (preço * 20 / 100)
        prestacao = juros / parcelas
        print(f'Sua compra será parcelada em {parcelas}x de R${prestacao:.2f} COM JUROS.')
        print(f'Sua compra de R${preço:.2f} vai custar R${juros:.2f} no final.')
else:
    print('\033[31mOPÇÃO INVÁLIDA!\033[m')

#Método Guanabara
#Este enfeite no código fiz de forma diferente ao de Guanabara
print('='*10, end='')
print(' LOJAS GUANABARA ', end='')
print('='*10)
preço = float(input('Preço das compras: R$'))
print('''FORMAS de PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 /100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f}')
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc}x de  R${parcela:.2f} COM JUROS')
print(f'Sua compra de R${preço:.2f} vai custar R${total:.2f} no final.')
