n = int(input('Digite um numero inteiro: '))
if n == 2 or n == 3 or n == 5:
    print('{} é um número primo'.format(n))
else:
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        print('{} não é um número primo'.format(n))
    else:
        print('{} é um número primo'.format(n))
