# as listas diferentes das tuplas, são mutaveis.
# para adicionar um, novo valor a lista deve se utilizar
# o comando .append()
# com o comando .insert(posição,produto), vc consegue adiconar
# um produto em uma posição ja existente, modificando a ordem da lista.
# para eliminar um produto da lista deve se utilizar o comando
#del nome da lista[numero do produto] ou o comando .pop(numero do produto)
# o comando .remove('nome do produto') ele tbm elimina um valor porem
# ele elimina pelo nome e nao pelo numero.
# valores = list(range(4,11)) (adiciona na lista valores os numeros de 4 ate 10
# o comando .sort() coloca os valores em ordem crescente.
# o comando .sort(reverse=True) deixa os valores em ordem decrescente
# o comando len(nome da lista) mostra o total de elementosda lista.
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.pop(2)
print(num)
print(f'Essa lista tem {len(num)} elementos')

print('=' * 30)
valores = []
#valores.append(5)
#valores.append(9)
#valores.append(4)
for c in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
print('=' * 30)

a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
# se igualar uma lista com outra, o python cria uma ligação
# entre elesa, assim se vc alterar uma a outra tbm se altera.
b = a[:] # com esse comando a lista b cria uma copia da lista a
#porem as duas não fazem nenhuma ligação.