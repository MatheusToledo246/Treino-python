#leia o salario, se for maior que 1250 vaiter aumento de 10%
#para salario menor o aumento é de 15%
n = float(input('Qual o salário do funcionário? R$'))
if n > 1250:
    s = n * 1.10
else:
    s = n * 1.15
print('Quem ganhava R${:.2f} passará á ganhar R${:.2f} agora.'.format(n, s))
