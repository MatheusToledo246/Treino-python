a = int(input('Escolha um ano: '))
if (a % 4) == 0 and (a % 100) == 0:
    print(' esse é um ano bissexto')
else:
    print('esse não é um ano bissexto')