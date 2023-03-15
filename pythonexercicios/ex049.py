#, mostrando a tabuada de um número que o usuário
# escolher, só que agora utilizando um laço for.
tb = int(input('Esolha uma tabuada: '))
for c in range(1, 11):
    print('{} X {:2} = {}'.format(tb, c, tb*c))

