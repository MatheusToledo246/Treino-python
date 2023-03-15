#Faça um programa que leia um número qualquer e
# mostre o seu fatorial.
#from math import factorial
#n = int(input('Digite um numero: '))
#f = factorial(n)
#print('O Fatorial de {} é {}'.format(n, f))
# para um calculo rapido pode se utilizar o módulo, porem so
#indicará o resultado final.
n = int(input('Digite um número para calcular seu fatorial: '))
c = n #c representa o contador
f = 1 #1 pq o fator nulo de mulplicação é 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)
print('-=' * 10, end='')
print(' FOR ', end='')
print('-=' * 10)
print('Calculando {}! = '.format(n), end='')
mult = 1
for m in range(n, 0, -1):
    print('{}'.format(m), end='')
    print(' X ' if m > 1 else ' = ', end='')
    mult *= m
print(mult)
