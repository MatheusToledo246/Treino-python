#ler o preço de produto e indicar o novo valor com 5% de desconto
m = float(input('Digite o valor do produto: '))
d = m - (m * 0.05)
print('O valor do produto com desconto de 5% é: R${:.2f}'.format(d))
#tambem pode se fazer m - (d = m * 5 / 100)
