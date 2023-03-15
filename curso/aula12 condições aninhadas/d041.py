from datetime import date
a = int(input('Qual seu ano de nascimento? '))
atual = date.today().year
cat = atual - a
if cat <= 9:
    print('Voce tem {} anos, então esta na categoria MIRIM'.format(cat))
elif cat <= 14:
    print('Você tem {} anos, então esta na categoria INFANTIL'.format(cat))
elif cat <= 19:
    print('Você tem {} anos então esta na categoria JUNIOR'.format(cat))
elif cat <= 20:
    print('Você tem {} anos, então esta na categoria SÊNIOR'.format(cat))
else:
    print('Você tem {} anos, então esta na categoria MASTER!'.format(cat))
