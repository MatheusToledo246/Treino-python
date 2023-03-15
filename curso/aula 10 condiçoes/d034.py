n = float(input('Qual seu salário atual? R$ '))
if n > 1.250:
    a = (n * 1.10)
    print('com o aumento de 10% seu salário agora é R$ {:.2f}'.format(a))
else:
    a = (n * 1.15)
    print('com o aumento e 15% seu salário agora é R$ {:.2f}'.format(a))
