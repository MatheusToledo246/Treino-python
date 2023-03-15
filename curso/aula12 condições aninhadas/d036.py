v = float(input('Qual o valor da casa? R$'))
s = float(input('Qual o salário do comprador? R$'))
a = int(input('Quantos anos pra pagar? '))
p = (v / (a * 12))
ex = (s * 0.30)
print('Para pagar uma casa de R${:.2f} em {} anos á prestação será de R${:.2f}'.format(v, a, p))
if p <= ex:
    print('Emprestimo Aprovado!')
else:
    print('Emprestimo Negado!')

