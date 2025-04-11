#Ler uma palavra e verificar se é um palíndromo

frase = str(input('Digite uma frase: ')).strip()
modi = frase.split() #Dividindo a frase
modi1 = ''.join(modi) #Juntando as partes sem os espaços


modi2 = ""
for c in frase[::-1]: #Forma de fazer o for digitar a frase de trás para frente
    print(c, end='') #Digitando a frase de trás para frente
    modi2 += c #Recebendo a frase digitada de trás para frente

print('\n')
modi = modi2.split() #Dividindo a frase
reverso = ''.join(modi) #Juntando as partes sem os espaços

if modi1.upper() == reverso.upper(): #Verificando se a frase é um palíndromo
    print('Essa frase é um palíndromo.')
    print(f'A palavra começando do inicio juntada, sem espaços: {modi1}')
    print(f'A palavra de trás pra frente juntada: {reverso}')
else:
    print('Essa frase não é um palíndromo.')
    print(f'A palavra começando do inicio juntada, sem espaços: {modi1}')
    print(f'A palavra de trás pra frente juntada: {reverso}')

#Método Guanabara
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
