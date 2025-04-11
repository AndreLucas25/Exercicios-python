#Ler largura e altura de uma parede e informar a quantidade de tinta necessária para pintá-la

largura = float(input('Largura: '))
altura = float(input('Altura: '))
area = altura*largura
print(f'A quantidade de tinta necessária pra pintá-la é {area/2}L')