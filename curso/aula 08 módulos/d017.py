from math import sqrt, hypot
co = float(input('Indique o valor do cateto oposto: '))
ca = float(input('Indique o valor do cateto adjacente: '))
#h = sqrt((co**2)+(ca**2))
h = hypot(co, ca)
print('A hipotenusa é igual á {:.2f}'.format(h))
