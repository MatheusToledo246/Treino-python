#: Crie um programa que leia o nome e o preço de
# vários produtos. O programa deverá perguntar se
# o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
print('-' * 30)
print('' * 10, 'Loja Super Store', '' * 10)
print('-' * 30)
soma = pm = pb = cont = 0
nb = ''
while True:
    nome = str(input('Nome do produto: ')).strip().upper()
    pc = float(input('Preço R$'))
    soma += pc
    cont += 1
    if cont == 1:
        pb = pc
        nb = nome
    if pc > 1000:
        pm += 1
    if pb > pc:
        nb = nome
        pb = pc
    cn = ' '
    while cn not in 'SN':
        cn = str(input('Quer continuar? [S/N] ')).strip().upper()
    if cn == 'N':
        break
print('-' * 10, 'FIM DO PROGRAMA', '-' * 10)
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {pm} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {nb} que custa {pb:.2f}')