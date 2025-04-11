#Ler a altura e peso de uma pessoa e calcular seu índice de massa corpora

#Meu método
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

if altura.is_integer():
    altura = altura / 100
imc = peso / (altura**2)

if 18.5 > imc:
    print(f'Seu imc é {imc:.1f}. Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print(f'Seu imc é {imc:.1f}. Você está no peso ideal.')
elif 25 <= imc < 30:
    print(f'Seu imc é {imc:.1f}. Você está sobrepeso.')
elif 30 <= imc < 40:
    print(f'Seu imc é {imc:.1f}. Você está na obesidade.')
elif imc >= 40:
    print(f'Seu imc é {imc:.1f}. Você está na obesidade mórbida.')

#Método Guanabara
peso = float(input('Qual é seu peso? (kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura * 2)
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('Parábens, Você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE!')
elif imc >=40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
