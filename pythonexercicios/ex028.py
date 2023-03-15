# tentar adivinhar o numero que amaquina pensou de 0 á 5
from random import randint
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
computador = randint(0, 5)#maquina vai escolher um valor
#print(computador)
n = int(input('em qual número eu pensei? '))# jogador tenta adivinhar
print('PROCESSANDO.....')
sleep(3)
if n == computador:
    print('Parabéns, vc venceu a máquina!!!')
else:
    print('Voce falhou, humano tolo!!!!')
    print("Eu pensei no número {} e não no número {}".format(computador, n))