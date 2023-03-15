primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1
total = 0
mt = 10
while mt != 0:
    total = total + mt
    while cont <= total:
        print('{} -> '.format(primeiro), end='')
        primeiro += razao
        cont += 1
    print('PAUSA')
    mt = int(input('Quantos termos você quer mostras a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))
