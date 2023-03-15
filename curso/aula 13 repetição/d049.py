n = int(input('Escolha uma tabuada:'))
for c in range(1, 11):
    tb = n * c
    print('{} X {} = {}'.format(n, c, tb))
