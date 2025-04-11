#Ler o nome de uma cidade e informar se ela começa com santo

#Meu método
city = str(input('Digite o nome de uma cidade: ')).strip().upper().capitalize()
print(f'{city} começa com Santo: {"Santo" in city[0:5]}')

#Método Guanabara
cid = str(input('Em que cidade você nasceu? '))
print(cid[:5].upper() == 'SANTO')