# Tuplas(variaveis compostas)
# variavel que guarda mais de um valor
#print(lanche[2])
#print(lanche[0:2])
#len(lanche)
#for c in lanche:
#   print(c)
#As tuplas são imutaveis (não da pra tirar
# uma variavel expecifica)
#lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim', 'batata Frita'
#print(lanche[0:])
#print(len(lanche))

#for cont in range(0, len(lanche)):
 #   print(f'Eu vou comer {lanche[cont]} na posição {cont}')

#for pos, comida in enumerate(lanche):
 #   print(f'Eu vou comer {comida} na posição {pos}')
#enumerate mostra o dado e a posição

#for comida in lanche:
 #   print(f'Eu vou comer {comida}')
#for comida in lanche:
 #   print(f'Eu vou comer {comida}')
#print('Comi pra caramba')

#print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(len(c))
print(c.count(5))# mostra a quantidades de numeros que tem
print(c.index(8))# ver a posição do numero, mostra so o primeiro valor
print(c.index(5, 1))# mostra todos os 5 partir da posição 1

pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa) # apaga totalmente a tupla
print(pessoa)