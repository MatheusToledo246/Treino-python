cont = 1
while True:
    print('-' * 20)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 20)
    if n < 0:
        break
    while cont <= 10:
        print(f'{n} X {cont} = {n * cont}')
        cont += 1
    cont = 1# depois de realizar a primeira tabuada o contevolta para valor 1
print('Tabuada encerrada. Volte sempre')

