# leia o ano de nascimento de um atleta e mostre
# sua categoria, de acordo com a idade, ate 9 mirim,
# até 14 infantil,até 19 junior, ate 25 senior, acima de 25 master
from datetime import date
an = int(input('Ano de nascimento: '))
at = date.today().year
idade = at - an
if idade <= 9:
    print('Você tem {} anos e sua categoria é MIRIM!'.format(idade))
elif idade <= 14:
    print('Você tem {} anos e sua categoria é INFANTIL!'.format(idade))
elif idade <= 19:
    print('Você tem {} anos e sua categoria é JÚNIOR!'.format(idade))
elif idade <= 25:
    print('Você tem {} anos e sua categoria é SÊNIOR!'.format(idade))
else:
    print('Você tem {} anos e sua categoria é MASTER'.format(idade))