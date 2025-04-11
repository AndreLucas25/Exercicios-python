#Ler o ano de nascimento de 7 pessoas e informar quantas já são maiores de idade e quantas não são
from datetime import date

maior = menor = 0
for c in range(1, 8):
    data = int(input('NASCIMENTO: '))
    idade = date.today().year - data
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'Tem {maior} pessoas que alcançou a maior idade e {menor} pessoas que ainda não alcançou.')

#Método Guanabara
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input(f'Em que ano a {pess}ª pessoa nasceu? '))
    idade = atual - nasc
    if idade  >= 21:
        totmaior +=1
    else:
        totmenor +=1
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade')
print(f'E também tivemos {totmenor} pessoas menores de idade')
