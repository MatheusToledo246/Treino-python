p = str(input('digite seu nome completo:')).strip()
nome = p.split()
print("primeiro nome: {}".format(nome[0]))
print('Ultimo nome: {}'.format(nome[len(nome)-1]))
#o split pega o nome e divide em pedaços separados por espaço
# utiliza o len pra saber quantas posições tem a lista nome
