t = int(input('Qual o primeiro termo? '))
r = int(input('Qual a razão? '))
decimo = t + (10 - 1) * r
for c in range(t, decimo + r, r):
    print('{}'.format(c), end='-> ')
print('Acabou')
#a formula utilizada no decimo serve pro for conseguir identificar
# os 10 primeiros termos de um PA
