# indique a hipotenusa de um triangulo retangulo
#from math import sqrt
import math
n = float(input('Comprimento do cateto oposto: '))
n2 = float(input('Comprimento do cateo adjacente: '))
# h = sqrt((n**2) + (n2**2))
h = math.hypot(n, n2)
print('A hipotenusa vai medir {:.2f}'.format(h))
# a biblioteca math realiza o calculod e hipotenusa com o
#math.hypot