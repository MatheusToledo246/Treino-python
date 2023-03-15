#import random
from random import shuffle
n1 = str(input('Indique o primeiro aluno: '))
n2 = str(input('Indique o Segundo aluno: '))
n3 = str(input('Indique o terceiro aluno: '))
n4 = str(input('Indique o quarto aluno: '))
lista = [n1, n2, n3, n4]
#random.shuffle(lista)
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)
# o suffle serve para embaralhar uma lista.