#import random
from random import choice
p = str(input('Primeiro aluno: '))
s = str(input('Segundo aluno: '))
t = str(input('terceiro aluno: '))
q = str(input('Quarto aluno: '))
lista = [p, s, t, q]
#e = random.choice(lista)
e = choice(lista)
print('O aluno escolhido foi {}'.format(e))
# a biblioteca ramdom serve para sortear um resulado.