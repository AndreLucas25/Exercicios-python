#Ler nome e preço de vários produtos, ao final, mostrar o total gasto, produtos acima de R$1000 e o produto mais baratos

#Titulo
print('_'*30) #Enfeite
print(f'LOJA SUPER BARATÃO') #Enfeite
print('_'*30) #Enfeite

#Criando variáveis
total = 0 #VAi receber a soma dos valores da compra
produto_mais1000 = 0 #Vai receber a quantidade de produtos acima de 1000
preço_mais_barato = 0 #Vai receber o valor do produto mais barato
nome_mais_barato = 0 #Vai receber o nome do produto mais barato
contador = 0 #Vai contar a repetição do looping

#Entrando no cadastramento de nome e valor do produto, até o usuário digitar "N" e o looping vai encerrar
while True:
    contador += 1 #Vai contar as repetições do looping
    produto = str(input('Nome do Produto: ')) #Vai ler o nome do produto
    preço = float(input('Preço: R$')) #Vai ler o preço do produto
    total += preço #Soma os valores dos produtos
    if preço > 1000: #Se o preço for maior de 1000, a variável abaixo vai receber +1
        produto_mais1000 += 1 #Recebendo +1
    if contador == 1: #Se o contador for igual a um, será o ínicio do looping, e as variáveis abaixo vai receber o nome e o valor do produto
        preço_mais_barato = preço #Recebendo o valor
        nome_mais_barato = produto #Recebendo o nome
    else: #Se não for igual a um, o looping não está no ínicio, aí irá haver a verificação
        if preço_mais_barato > preço: #Se o valor da variável preço_mais_barato foi maior que a variável preço, ela então receberá o preço e a outra o nome
            preço_mais_barato = preço #Recebendo o preço
            nome_mais_barato = produto #Recebendo o nome
    flag = str(input('Deseja continuar? [S/N] ')).strip().upper()[0] #Perguntando se o usuário deseja continuar
    if flag == 'N': #Se a resposta for 'N', sai do looping
        print('===== FIM DO PROGRAMA =====') #Enfeite
        break #Saindo do looping

#Saida de dados
print(f'O total de compra foi R${total:.2f}')
print(f'Temos {produto_mais1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_mais_barato} que custa R${preço_mais_barato:.2f}')