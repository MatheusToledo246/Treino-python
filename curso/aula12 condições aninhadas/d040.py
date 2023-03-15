n = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n + n2) / 2
if m < 5.0:
    print('REPROVADO!')
elif 5.0 <= m <= 6.9:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')
