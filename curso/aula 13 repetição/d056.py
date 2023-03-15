media = 0
velho = 0
nv = ''
idadef = 0
for c in range(1, 4+1):
    nome = str(input('Qual seu nome? '))
    idade = int(input('Quantos anos você tem? '))
    sx = str(input('Qual seu Sexo?(MASCULINO/FEMININO) ')).upper()
    print('Obrigado !!!')
    media += idade
    if sx == 'MASCULINO' and idade > velho:
        velho = idade
        nv = nome
    if sx == 'FEMININO' and idade < 20:
        idadef += 1
print('A média de idade nesse grupo de pessoas é de {:.0f} anos'.format(media / 4))
print('O homem mais velho se chama {} e tem {} anos'.format(nv, velho))
print('{} Mulher(es) tem menos de 20 anos.'.format(idadef))
