midade = homem = mulheres = 0
cont = 1
while True:
    print('=-' * 10)
    print(f'CADASTRO DA {cont}° PESSOA')
    print('=-' * 10)
    idade = int(input('Idade: '))
    sx = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while 'M' != sx != 'F':
        sx = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('=-' * 10)
    user = str(input('Deseja continuar? ')).strip().upper()[0]
    while 'S' != user != 'N':
        user = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if idade > 18:
        midade += 1
    if sx == 'M':
        homem += 1
    if sx == 'F' and idade < 20:
        mulheres += 1
    if user == 'N':
        break
    cont += 1
print('===== FIM DO PROGRAMA =======')
print(f'{midade} Pessoas tem mais de 18 anos.')
print(f'foram cadastrados {homem} homens.')
print(f'{mulheres} mulheres tem menos de 20 anos.')