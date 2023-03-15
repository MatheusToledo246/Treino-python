#leia a velocidade, se for maior que 80 pegar uma multa.
# a multa é R$ 7,00 pra cada km acima de 80.
n = float(input('Qual a velocidade atual do carro? '))
if n > 80:
    print('multado! Você excedeu o limite permitido de 80km/h')
    m = (n - 80) * 7
    print('á multa custará R$ {:.2f}'.format(m))
print('Tenha um Bom dia! dirija com segurança!!!')
