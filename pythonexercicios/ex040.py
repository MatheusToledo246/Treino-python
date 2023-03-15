n = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n + n2) / 2
if m < 5:
    print('Sua média foi {:.1f}, então você está REPROVADO!'.format(m))
elif 5 <= m <= 6.9:
    print('Sua média foi {:.1f}, então voce está de RECUPERAÇÃO!'.format(m))
else:
    print('Sua média foi {:.1f}, então você está APROVADO!'.format(m))