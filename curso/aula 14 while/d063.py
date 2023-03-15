print('-' * 20)
print('Sequência de Fibonacci')
print('-' * 20)
n = int(input('Quantos termos você quer mostrar? '))
#os dois primeiros termos são definidos automaticamnete.
t1 = 0
t2 = 1
print('~' * 20)
print('{} -> {}'.format(t1, t2), end='')
cont = 3# o contador começa no 3 pois ja tem os dois primeiros valores
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> Fim')
