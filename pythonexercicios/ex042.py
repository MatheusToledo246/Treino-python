# calcule os 3 segmentos de um triangulo e diga se ele é
# equilatero,iosceles ou escaleno
p = float(input('Primeiro Segmento: '))
s = float(input('Segundo Segmento: '))
t = float(input('Terceiro Segmento: '))
if p + s > t and p + t > s and t + s > p:
    if p == s == t:
        print("Esse triângulo é um EQUILÁTERO.")
    elif p != s != t != p:
        print('Esse triângulo é um ESCALENO.')
    else:
        print('Esse triângulo é um ISÓCELES.')
else:
    print('Esses segmentos não formam um triângulo;')
