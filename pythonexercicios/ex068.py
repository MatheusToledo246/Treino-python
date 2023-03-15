#Faça um programa que jogue par ou ímpar com o
# computador. O jogo só será interrompido quando
# o jogador perder, mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo.
from random import randint
v = soma = 0
print('=-' * 20)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 20)
computador = randint(1, 10)
while True:
    pi = ''
    n = int(input('Diga um valor: '))
    while 'P' != pi != 'I':
        pi = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print('-' * 20)
    soma = n + computador
    if soma % 2 == 0:
        print(f'Você jogou {n} e o computador {computador}. Total de {soma} Deu Par')
    else:
        print(f'Você jogou {n} e o computador {computador}. Total de {soma} Deu Impar')
    print('-' * 20)
    if pi == 'P' and soma % 2 == 0:
        print('Você venceu!')
        print('Vamos jogar novamente....')
        v += 1
        print('=-' * 20)
    elif pi == 'I' and soma % 2 != 0:
        print('Você venceu!')
        print('Vamos jogar novamente....')
        v +=1
        print('=-' * 20)
    else:
        print('Você perdeu!')
        break
print(f'GAMR OVER! Você venceu {v} vezes')