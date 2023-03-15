# Crie um programa que leia a idade e o sexo de
# várias pessoas. A cada pessoa cadastrada, o
# programa deverá perguntar se o usuário quer
# ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
print('-' * 30)
print('' * 2, 'CADASTRE UMA PESSOA', '' * 2)
print('-' * 30)
tt = hm = ml = 0
while True:
    id = int(input('Idade: '))
    sx = str(input('Sexo: [M/F] ')).upper().strip()
    print('-' * 30)
    ct = str(input('Quer continuar? [S/N] ')).strip().upper()
    print('-' * 30)
    if id > 18:
        tt += 1
    if sx == 'M':
        hm += 1
    if sx == 'F' and id < 20:
        ml += 1
    if ct == 'N':
        break
print(f'Total de pesoas com mais de 18 anos : {tt}')
print(f'Ao todo temos {hm} homens cadastrados')
print(f'E temos {ml} Mulheres com menos de 20 anos.')