# mostre o dobro, triplo e a rai\ quadrada de n
n = int(input('Digite um número: '))
#d = n * 2
#t = n * 3
#r = n **(1/2)
#print('Analisando o valor {} \nSeu dobro é {} \nSeu triplo é {}\nsua raiz quadrada é {}'.format(n, d, t, r))
# outra forma de calcular a raiz é utilizar o pow(n, (1,2)) dentro do format
#sendo n o valor base e o 1,2 o valor de cima da potencia.
print('o dobro de {} vale {}'.format(n, (n*2)))
print('O triplo vale {} e a raiz vale {}'.format((n*3), pow(n, (1/2))))
