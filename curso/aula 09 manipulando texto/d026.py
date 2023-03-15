p = str(input('Escreva uma frase: ')).upper().strip()
print('á letra "A" aparece {} vezes'.format(p.count('A')))
print(' a letra "A" aparece na posição {}'.format(p.find('A')+1))
print('A letra "A" aparece pela ultima vez na posição {}'.format(p.rfind('A')+1))
# é necessario somar +1 pos a posição inicial é = 0
# o strip é utilizado pra eliminar os espaços para que não de erro