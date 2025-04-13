#Ler o valor de um produto, e ajustar o valor conforme a forma de pagamento

#Meu método
preço = float(input('Preço das compras: R$')) #Lendo o valor das compras
pagamento = int(input('''FORMAS DE PAGAMENTO 
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
Qual é a opção? ''')) #Menu com as opções de pagamento pro usuário fazer

if pagamento == 1: #Se a opção escolhida for 1, ele terá 10% de desconto
    desconto = preço - (preço * 10 / 100) #Calculo do desconto
    print(f'Sua compra de R${preço:.2f} vai custar R${desconto:.2f} no final.') #Saida de dados
elif pagamento == 2: #Se a opção escolhida for 2, ele terá 5% de desconto
    desconto = preço - (preço * 5 / 100) #Calculo do desconto
    print(f'Sua compra de R${preço:.2f} vai custar R${desconto:.2f} no final.') #Saida de dado
elif pagamento == 3: #Se a opção escolhida for 3, a compra continua no mesmo valor
    print(f'Sua compra continua custando R${preço:.2f}') #Saida de dados
elif pagamento == 4: #Se a opção dele for a 4, ele escolhe quantas parcelas vai ser
    parcelas = int(input('Quantas parcelas? ')) #Lendo a quantidade de parcelas
    if parcelas <= 2: # Se a parcela for menor ou igual a dois, será o mesmo valor
        print(f'Sua compra continua custando R${preço:.2f}') #Saida de dados
    else: #Se não for menor ou igual a dois, é maior, sendo assim o valor receberá 30% de juros
        juros = preço + (preço * 20 / 100) #Calculo do juros
        prestacao = juros / parcelas #Valor da prestação com o juros aplicado
        print(f'Sua compra será parcelada em {parcelas}x de R${prestacao:.2f} COM JUROS.') #Saida de dados
        print(f'Sua compra de R${preço:.2f} vai custar R${juros:.2f} no final.') #Saida de dados
else:
    print('\033[31mOPÇÃO INVÁLIDA!\033[m') #Se ele digitar qualquer número que não equivala as opções que tem lá, receberá uma mensagem de erro

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
