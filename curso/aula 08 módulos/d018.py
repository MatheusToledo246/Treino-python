import math
n = float(input('Indique o ángulo: '))
s = math.sin(math.radians(n))
c = math.cos(math.radians(n))
t = math.tan(math.radians(n))
print('angulo indicado: {} \nSeno: {:.2f} \nCosseno: {:.2f} \nTangente: {:.2f}'.format(n, s, c, t))
#o valor de dentro dos parenteses tenq ser convertido em radianos.