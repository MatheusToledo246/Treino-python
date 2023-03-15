soma = 0
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        soma += n
print('O resultado da soma é {}'.format(soma))
