maior = 0
menor = 10000000
for c in range(1, 5+1):
    p = float(input("qual seu peso? "))
    if p > maior:
        maior = p
    if p < menor:
        menor = p
print('o maior peso foi {:.1f} Kg'.format(maior))
print('O menor peso foi {:.1f} Kg'.format(menor))
