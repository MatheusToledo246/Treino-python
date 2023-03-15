p = float(input('qual o preço do produto? R$'))
f = str(input('Qual a forma de pagamento? '))
if f == 'dinheiro' or f == 'cheque':
    print('Sua compra á vista no Dinheiro ou no Cheque tem '
          '10% de desconto')
    print('você pagará somente R${:.2f}'.format(p - (p * 0.10)))
elif f == 'cartao':
    print('Sua compra á vista no Cartão tem 5% de desconto')
    print('Você pagará somente R${:.2f}'.format(p - (p * 0.05)))
elif f == '2xcartao':
    print('sua compra em 2x no cartão tem o preço normal')
    print('Você pagará R${:.2f}'.format(p))
elif f == '3xmais':
    print('Para compras acima de 3x no cartão tem um juros'
          ' adicional de 20%')
    print('Você pagará R${:.2f}'.format(p * 1.20))
