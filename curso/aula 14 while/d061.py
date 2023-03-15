t = int(input('Qual o primeiro termo? '))
r = int(input('Qual a razão? '))
#termo = t
cont = 1
while cont <= 10:
    print('{} -> '.format(t), end='')
    t += r
    cont += 1
print('Fim')
#principal diferença do wilhe é so precisa indicar o laço
#o for vc utiliza o laço na contagem

'''decimo = t + (10 - 1) * r
for c in range(t, decimo + r, r):
    print('{}'.format(c), end='-> ')
print('Acabou')'''
#a formula utilizada no decimo serve pro for conseguir identificar
# os 10 primeiros termos de um PA
