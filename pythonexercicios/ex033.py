# leia 3 valores e imdique o maior e o menor deles
n = int(input('Indique um valor: '))
n2 = int(input('Indique um segundo valor: '))
n3 = int(input('Indique um tercerio valor: '))
#verificando o maior
maior = n
if n2 > n and n2 > n3:
    maior = n2
elif n3 > n and n3 > n2:
    maior = n3
print('o maior valor é {}'.format(maior))
#verificando o menor
menor = n
if n2 < n and n2 < n3:
    menor = n2
elif n3 < n and n3 < n2:
    menor = n3
print('o menor valor é {}'.format(menor))
