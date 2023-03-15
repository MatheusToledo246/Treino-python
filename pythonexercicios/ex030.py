# leia um número e indique se ele é par ou impar.
n = int(input('Diga um número: '))
if n % 2 == 0:
    print('{} é um número é par'.format(n))
else:
    print('{} é um número impar'.format(n))
