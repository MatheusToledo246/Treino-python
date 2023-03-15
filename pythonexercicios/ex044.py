#calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de
# pagamento, à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros
print('========== LOJAS MATTECNOLOGI ==========')
p = float(input('Preço das compras R$'))
fp = int(input('''FORMA DE PAGAMENTO
[ 1 ] à vista em dinheiro\cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual opção desejada? '''))
if fp == 1:
    desc = p - (p * 0.10)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(p, desc))
elif fp == 2:
    desc = p - (p * 0.05)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(p, desc))
elif fp == 3:
    par = p / 2
    print('Sua compra será parcelada em 2x de R${} SEM JUROS.'.format(par))
elif fp == 4:
    qp = int(input('Quantas parcelas? '))
    par = p / qp
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(qp, par))
    print('Sua compra de R${} vai custar R${:.2f} no final.'.format(p, p * 1.20))
else:
    print('Erro, Opção invalida.')