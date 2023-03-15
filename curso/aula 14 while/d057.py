sx = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]
#utiliza-se o [0] pra trabalahr com a primeira letra
while sx not in 'MF':
    sx = str(input('Dados invalidos. Por favor, informe seu sexo:')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sx))

