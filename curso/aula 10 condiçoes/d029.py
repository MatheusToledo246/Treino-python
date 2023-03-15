v = float(input('Qual a velocidade do carro? '))
if v > 80:
    print('você foi multado!!!')
    m = (v - 80) * 7
    print('Sua multa foi de R$ {}'.format(m))
else:
    print('O carro esta dentro do limite de velocidade.')
