from random import randint
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)
cp = randint(0, 10)
pi = computado = ''
n = resolt = 0
vencedor = 0
cont = 0
while True:
    n = int(input('Diga um valor: '))
    pi = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    resolt = cp + n
    if resolt % 2 == 0:
        print(f'Você jogou {n} e o computador {cp}. Total de {resolt} DEU PAR')
    else:
        print(f'Você jogou {n} e o computador {cp}. Total de {resolt} DEU IMPAR')
    if pi == 'P' and resolt % 2 == 0 or pi == 'I' and resolt % 2 != 0:
        vencedor = 1
        cont += 1
        print('Você VENCEU!')
    else:
        vencedor = 2
        print('Você PERDEU!')
        print('=-' * 20)
    if vencedor == 1:
        print('Vamos jogar novamente...')
        print('=-' * 20)
        vencedor = 0
    if vencedor == 2:
        break
print(f'Game over! Você venceu {cont} vezes.')