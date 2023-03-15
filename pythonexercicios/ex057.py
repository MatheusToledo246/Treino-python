#Faça um programa que leia o sexo de uma pessoa, mas
# só aceite os valores ‘M’ ou ‘F’. Caso esteja errado,
# peça a digitação novamente até ter um valor correto.
sx = str(input('Qual seu sexo? [M/F]')).upper().strip()[0]
while sx not in 'MF':
    sx = str(input('Dados inválidos. Por favor, informe seu sexo: ')).upper().strip()[0]
print('Sexo {} registrado com sucesso'.format(sx))
