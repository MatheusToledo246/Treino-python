#endo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão
# usando a estrutura while.
print('Gerador de PA')
print('-=' * 10)
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = n
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += r
    cont += 1
print('Fim')
