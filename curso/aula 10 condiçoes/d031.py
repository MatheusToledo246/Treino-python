n = float(input('Quantos a distancia em km que vc quer ir? '))
if n <= 200:
    p = (n * 0.50)
    print('o preço da passagem será de 0,50 centavos por km')
    print('o preço da sua passagem é de R${}'.format(p))
else:
    p = (n * 0.45)
    print('o preço da passagem será de 0,45 centavos por km')
    print('o preço da sua passagem será de R$ {}'.format(p))