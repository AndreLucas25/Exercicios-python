#Achando a hipotenusa
import math

c1 = float(input('Digite a medida do cateto adjacente: '))
c2 = float(input('Digite a medida do cateto oposto: '))
hipotenusa = math.hypot(c1, c2)
print(f'A hipotenusa é {hipotenusa:.2f}')

co = float(input('Digite a medida do cateto oposto: '))
ca = float(input('Digite a medida do cateto adjacente: '))
hi = (co ** 2 + ca **2) ** (1/2)
print(f'A hipotenusa mede {hi:.2f}')
