for c in range(1, 7):
    print(c)
print('Fim')
for c in range(6, 0, -1):
    print(c)
print('Fim')
#para fazer o for contrar de tras pra frente é so
# adicionar o -1
for c in range(0, 7, 2):
    print(c)
print('fim')
#para fazer o for pular um numero é so adicionar
# a quantidade como terceiro numero.
n = int(input('Digite um numero: '))
for c in range(0, n):
    print(c)
print('Fim')
n = int(input('Digite um numero: '))
for c in range(0, n+1):
    print(c)
print('Fim')
# o n+1 serve pra fazer o for contar exatamente
# ate o numero em que o usuario digitou, pois normalmente
# o for para sempre um numero antes

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('fim')
s = 0
for c in range(0, 3):
    n = int(input('Digite um valor:'))
    s += n
print('O somatorio e todos os valores foi {}'.format(s))

