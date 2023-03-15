from datetime import date
a = int(input('Digite seu ano de nascimento: '))
idade = (date.today().year - a)
if idade < 18:
    tempo = 18 - idade
    print('você ainda vai se alistar!')
    print('faltam {} anos pra você se alistar!'.format(tempo))
elif idade == 18:
    print('Parabens, está na hora de você se alistar!')
else:
    tempo = idade - 18
    print('Já passou da sua hora de se alistar ')
    print('já se passaram {} anos do seu alistamento!'.format(tempo))

