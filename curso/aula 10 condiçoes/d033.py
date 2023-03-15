n = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
n3 = float(input('Digite o terceiro numero: '))
if n > n2 and n > n3:
    print(' o maior é o {}'.format(n))
elif n2 > n and n2 > n3:
    print('o maior é o {}'.format(n2))
else:
    print('o maior é o {}'.format(n3))
if n < n2 and n < n3:
    print('o menor é o {}'.format(n))
elif n2 < n and n2 < n3:
    print('o menor é o {}'.format(n2))
else:
    print('o menor é o {}'.format(n3))

