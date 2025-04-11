#Simular um caixa eletrõnico
#Não conseguir desenvolver uma solução propria, olhei os comentários e entendi uma forma interessante que foi a de baixo



#Solução dos comentários
print('='*20)
print('BANCO LC')
print('='*20)

saque = int(input('Digite o valor que deseja sacar: R$ '))
n50 = n20 = n10 = n1 = 0
while True:
    if saque >= 50:
        saque -= 50
        n50 += 1
    else:
        if saque >= 20:
            saque -= 20
            n20 += 1
        else:
            if saque >= 10:
                saque -= 10
                n10 += 1
            else:
                if saque >= 1:
                    saque -= 1
                    n1 += 1
    if saque == 0:
        break
print(f'''{n50} notas de R$50
{n20} notas de R$20
{n10} notas de R$10
{n1} notas de R$1.''')

