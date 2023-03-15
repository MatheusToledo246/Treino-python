n = 0
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if n < 0 or n > 20:
        print('tente novamente. ', end='')
    else:
        break
extenso = ('zero', 'um', 'dois', 'Três', 'Quatro','cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'Treze', 'quatorze', 'quinze', 'deseseis', 'desesete','dezoito', 'desenove', 'vinte')
print(f'Voce digitou o número {extenso[n]}')
