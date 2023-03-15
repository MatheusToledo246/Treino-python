#receber o salario e indicar o novo valor com 15%
# de aumento
n = float(input('Indique seu salário atual: R$ '))
a = (n * 1.15)
print('Com o aumento de 15% seu sálario de R${} passará a ser de R${:.2f}'.format(n, a))
# tambem pode fazer a = n + (n * 15 / 100)