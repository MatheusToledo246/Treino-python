tg = qc = pb = 0
cont = 1
barato = ''
print('--' * 30)
print(' ' * 19, 'CARRINHO DE COMPAS', ' ' * 19)
print('--' * 30)
while True:
    np = str(input(f'Nome do {cont}º produto: '))
    pc = float(input('Preço: R$'))
    user = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while 'S' != user != 'N':
        user = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    tg += pc
    if cont == 1:
        pb = pc
        barato = np
    if pb > pc:
        barato = np
        pb = pc
    if pc > 1000:
        qc += 1
    if user == 'N':
        break
    cont += 1
print('-' * 21, 'Fim DO PROGRAMA', '-' * 21)
print(f'O total gasto na compra é de R${tg:.2f}')
print(f'{qc} custam mais de R$1000.00')
print(f'O {barato} é o produto mais barato, pois custa R${pb:.2f}')



