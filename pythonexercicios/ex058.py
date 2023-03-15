#computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até
# acertar, mostrando no final quantos palpites foram
# necessários para vencer.
from random import randint
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
computador = randint(0, 10)#maquina vai escolher um valor
#print(computador)
n = int(input('em qual número eu pensei? '))# jogador tenta adivinhar
cont = 1
while n != computador:
    cont += 1
    print('PROCESSANDO.....')
    sleep(2)
    if n > computador:
        print('Menos....', end='')
    elif n < computador:
        print('Mais...', end='')
    print('tente novamente.')
    n = int(input('qual seu palpite? '))
print('Parabéns, vc venceu a máquina!!!')
print('Acertou com {} tentativas'.format(cont))
#pode se utilizar o
# acertou = false
# while not acertou:
#para fechar ese laço tenq indicar quem quando computado == n
#acertou = True.