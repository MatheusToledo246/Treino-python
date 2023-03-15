n = int(input("digite um valor: "))
parar = ''
cont = 1
media = n
maior = 0
menor = 10000000000000000000000000000000
parar = str(input('Deseja continuar? [SIM/NÃO] ')).upper().strip()
while parar not in 'NAONÃO':
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    n = int(input("digite um valor: "))
    parar = str(input('Deseja continuar? [SIM/NÃO] ')).upper().strip()
    cont += 1
    media += n
print('á média entre os valores é {:.1f}'.format(media / cont))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))