#Desenvolva um programa que leia o nome, idade e
# sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem
# mais velho e quantas mulheres têm menos de 20 anos.
midade = 0
velho = 0
nomv = ''
idadem = 0
for c in range(1, 5):
    print('----- {}° PESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sx = str(input('Sexo [M/F]: ')).upper().strip()
    midade += idade
    if sx == 'M' and idade > velho:
        velho = idade
        nomv = nome
    if sx == 'F' and idade < 20:
        idadem += 1
print('A média de idade do grupo é de {} anos'.format(midade / 4))
print('O homen mais velho tem {} anos e se chama {}'.format(velho, nomv))
print('Ao todo são {} mulheres com menos de 20 anos'.format(idadem))