#lei a disteancia e indique o preço da passagem, ate 200km o valor
#é de 0,50 centavos por km e acima de 200 o valor é de 0,45
n = float(input('Qual a distância da viagem? '))
print('Sua viagem tem {}Km.'.format(n))
#if n <= 200:
#    p = n * 0.50
#else:
#    p = n * 0.45
p = n * 0.50 if n <= 200 else n * 0.45
print('o valor da passagem será de R${:.2f}'.format(p))
# maneira simplificada economiza linhas porem é mais confuso.