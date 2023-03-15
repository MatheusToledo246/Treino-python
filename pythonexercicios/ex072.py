#Crie um programa que tenha uma dupla totalmente preenchida
# com uma contagem por extenso, de zero até vinte. Seu
# programa deverá ler um número pelo teclado (entre 0 e 20)
# e mostrá-lo por extenso.
numeros = 'zero', 'um', 'dois', 'três', 'Quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',\
    'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'deseseis', 'desesete', 'dezoito', 'dezenove', 'vinte'
n = 0
while True:
    n = int(input('Digite um número: '))
    if n < 0 or n > 20:
        print('Tente Novamente. ', end='')
    else:
        break
print(f'Você digitou o número {numeros[n]}')
