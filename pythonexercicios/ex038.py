# leia 2 numeros e diga qual é o maior ou se os 2
# são iguais
n = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
if n > n2:
    print('O Primeiro valor é maior')
elif n2 > n:
    print('o Segundo valor é maior')
else:
    print('não existe valor maior, os dois são iguais')