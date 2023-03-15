# ler o nome completo e indicar o primeiroe o ultimo nome
p = str(input('Digite seu nome completo: ')).strip()
lista = p.split()
print('Muito prazer em te conhecer!!!')
print('Seu primeiro nome é {}'.format(lista[0]))
print('Seu último nome é {}'.format(lista[len(lista)-1]))
