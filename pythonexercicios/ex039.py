# leia o ano de nascimento e indique se precisa se alistar
# ou quanto tempo falta pra se alisatr ou se ja se alistou
# a quanto tempo.
from datetime import date
an = int(input('Ano de nascimento: '))
sx = str(input('Gênero(Masculino, Feminino): ')).upper()
at = date.today().year
idade = at - an
if sx == 'MASCULINO':
    print('Quem nasceu em {} tem {} anos em {}'.format(an, idade, at))
    if idade < 18:
        ia = 18 - idade
        print('Ainda faltam {} anos para o alistamento'.format(ia))
        print('Seu alistamento será em {}.'.format(at + ia))
    elif idade == 18:
        print('Você deve se alistar IMEDIATAMENTE!')
    else:
        ia = idade - 18
        print('Você ja deveria ter se alistado á {} anos.'.format(ia))
        print('seu alistamento foi em {}.'.format(ia, at - ia))
elif sx == 'FEMININO':
    print('Você não precisa fazer alistamento militar.')
else:
    print('Erro, opção inválida!!!')
