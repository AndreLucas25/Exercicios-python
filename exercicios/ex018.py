#Ler um angulo e mostrar o seno, cosseno e tangente
import math

angulo_graus = int(input('Digite o angulo: °'))
angulo_radianos = math.radians(angulo_graus)

seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)
print(f'Seno de {angulo_graus} é {seno}\n'
      f'Cosseno de {angulo_graus} é {cosseno}\n'
      f'Tangente de {angulo_graus} é {tangente}')