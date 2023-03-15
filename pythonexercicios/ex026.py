# quantas vezes aparece a letra A em uma frase, qual posição
#aparece a primeira letra A e a posição da ultima letra A.
p = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase.'.format(p.count("A")))
print('A primeira letra A apareceu na posição {}'.format(p.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(p.rfind('A')+1))
#find conta até aparecer a letra do ()