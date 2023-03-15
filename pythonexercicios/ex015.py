# calcule o valor final de um carro alugado, sabendo
#que ele custa R$60 por dia e R$0,15 por km
d = int(input('Quantos dias alugados? '))
k = float(input('Quantos Km rodados? '))
p = (d * 60) + (k * 0.15)
print('Total á pagar é de R$ {:.2f}'.format(p))
