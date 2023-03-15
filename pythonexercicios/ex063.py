#Escreva um programa que leia um número N
# inteiro qualquer e mostre na tela os N primeiros
# elementos de uma Sequência de Fibonacci.
print('-' * 40)
print('Sequência de Fibonacci')
print('-' * 40)
n = int(input('Quantos termos você quer mostras? '))
print('~' * 40)
t1 = 0
t2 = 1
termos = n
cont = 3
t3 = 1
print('{} -> {} -> '.format(t1, t2), end='')
while cont <= n:
    t3 = t1 + t2
    print('{} -> '.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('Fim')
print('~' * 40)
