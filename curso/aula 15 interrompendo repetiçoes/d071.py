print('=' * 30)
print(' ' * 10, 'BANCO MT', ' ' * 10)
print('=' * 30)
n = int(input('Que valor você quer sacar? R$'))
cont = 1
calc = 0
while True:
    if cont == 1:
        calc = n
    if calc >= 50:
        calc = n % 50
        ced = n // 50
        print(f'Total de {ced} cédulas de R$50')
    if calc >= 20:
        ced = calc // 20
        calc = calc % 20
        print(f'Total de {ced} cédulas de R$20')
    if calc >= 10:
        ced = calc // 10
        calc = calc % 10
        print(f'Total de {ced} cédulas de R$10')
    if calc >= 1:
        ced = calc // 1
        calc = calc % 1
        print(f'Total de {ced} cédulas de R$1')
    cont += 1
    if calc == 0:
        break
print('=' * 30)
print('Volte sempre ao BANCO MT! Tenha um bom dia!')

