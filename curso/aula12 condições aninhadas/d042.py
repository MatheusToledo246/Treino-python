n = float(input('Quanto mede o Primeiro lado? '))
n2 = float(input('Quanto mede o Segundo lado? '))
n3 = float(input('Quanto mede o Terceiro lado? '))
if n + n2 > n3 and n2 + n3 > n and n + n3 > n2:
    if n == n2 == n3:
        print('Esse triangulo é um EQUILÁTERO ')
    elif n == n2 or n2 == n3 or n == n3:
        print('Esse triângulo é um ISÓCELES')
    else:
        print('Esse triângulo é um ESCALENO')
else:
    print('não forma um triângulo!')