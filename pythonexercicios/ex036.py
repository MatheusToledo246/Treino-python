# pergunte o valor da casa, salario do comprador e em quantos
#anos ele vaipagar.
#a prestação mensal nao pode exceder 30% do salario,ou entao deve
#negar o emprestimo
vc = float(input('Qual o valor da casa? '))
sl = float(input('qual o seu salário? '))
ap = int(input('Vai pagar em quantos anos? '))
prest = vc / (ap * 12)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação'
          ' será de {:.2f}'.format(vc, ap, prest))
#se adicionar o end='' no final do print, ele unta 2 linhas em
#uma.
if prest > (sl * 0.30):
    print('Emprestimo NEGADO!')
else:
    print('Emprestimo APROVADO!')
