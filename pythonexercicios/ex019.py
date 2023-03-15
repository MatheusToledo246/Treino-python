# sortear entre as variaveis quem vai limpar a lousa
import random
p = str(input('Primeiro aluno: '))
s = str(input('Segundo aluno: '))
t = str(input('Terceiro aluno: '))
q = str(input('Quarto aluno:'))
lista = [p, s, t, q]
print('Quem vai limpar á lousa é {}'.format(random.choice(lista)))
#lista semopre tenq ficar com [] couchetes
# para sortear deve se utilizar a biblioteca random
# para se sortear utilize o comando random.choice()