# faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
computador = randint(0, 2)
itens = ('Pedra', 'Papel', 'Tesoura')
p = int(input('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é a sua jogada? '''))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('=-'*20)
print('O computador escolheu {}'.format(itens[computador]))
print('Você escolheu {}'.format(itens[p]))
print('=-' * 20)
if p == 0 and computador == 2 or p == 1 and computador == 0 or p == 2 and computador == 1:
    print('Você venceu!')
elif p == computador:
    print('Empate!')
else:
    print('O computador venceu!')
