from random import choice
from time import sleep
sorteio = ('PEDRA', 'PAPEL', 'TESOURA')
m = choice(sorteio)
print('-='*20)
print('ESCOLHA UM DOS DOS 3 \n[ PEDRA ] \n[ PAPEL ] \n[ TESOURA ]' )
print('-=' * 20)
r = str(input('Qual você escolhe: ')).upper()
if r == m:
    print('JO')
    sleep(1)
    print('ken')
    sleep(1)
    print('PO')
    print('-=' * 20)
    print('Empate >.<')
    print('Eu joguei {} e Você jogou {}'.format(m, r))
elif r == 'PEDRA' and m =='TESOURA' or r == 'TESOURA' and m == 'PAPEL' or r == 'PAPEL' and m == 'PEDRA':
    print('JO')
    sleep(1)
    print('ken')
    sleep(1)
    print('PO')
    print('-=' * 20)
    print('Você me venceu!!!!!')
    print('Eu joguei {} e Você jogou {}'.format(m, r))
elif m == 'PEDRA' and r == 'TESOURA' or m == 'TESOURA' and r == 'PAPEL' or m == 'PAPEL' and r == 'PEDRA':
    print('JO')
    sleep(1)
    print('ken')
    sleep(1)
    print('PO')
    print('-=' * 20)
    print('Eu ganhei!!!')
    print('Eu joguei {} e Você jogou {}'.format(m, r))
else:
    print('Erro, escolha invalida!')


