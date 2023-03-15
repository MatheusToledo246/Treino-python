#Desenvolva um programa que leia quatro valores pelo teclado
# e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
n = (int(input('Digite um valor: ')), int(input('Digite um valor: ')),
     int(input('Digite um valor: ')), int(input('Digite um valor: ')))
print(n)
print(f'o número 9 apareceu {n.count(9)} vezes') # o count serve para contar quantas vezes apreceu determinado valor
if 3 in n:
    print(f'O valor 3 aparece primeiro na {n.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print(f'Os valores pares digitados foram: ', end='')
for num in n:
    if num % 2 == 0:
        print(num, end=' ')
