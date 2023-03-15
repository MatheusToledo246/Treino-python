#indique a tabuada de um numero
n = int(input('digite qual tabuada vc deseja: '))
print('-' * 12)
print('{} X {:2} = {} \n{} X {:2} = {} \n ....... \n{} X {:2} = {}'.format(n, 1, n * 1, n, 2, n * 2, n, 10, n*10))
print('-' * 12)