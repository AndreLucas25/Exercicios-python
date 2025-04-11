#Fazer um programa que faça uma contagem regressiva com um espaço de um segundo entre os números
from time import sleep
import emoji

print('Os fogos vai começar em...')
sleep(1)
for c in range(10, 0, -1):
    print(c)
    sleep(1)
fogos = emoji.emojize("Boom! :fireworks:")
print(fogos)

#Método Guanabara
for cont in range(10, 0, -1):
    print(cont)
    sleep(0.5)
print('BUM! BUM! POOOW!')