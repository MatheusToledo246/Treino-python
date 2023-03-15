from random import randint
computador = randint(0, 5) # Faz o computador "PENSAR"
#print('Pensei em um número {}'.format(computador))
print('-=-' * 20)
print('Vou pensar em um numero entre 0 á 5, Tente adivinhar....')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? ')) # jogador tenta adivinhar
if jogador == computador:
    print('Parabens você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no numero {} e não no numero {}'.format(computador, jogador))
