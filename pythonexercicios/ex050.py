soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {} valor inteiro: '.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Forma escolhidos {} numeros pares, e a soma deles é {}'.format(cont, soma))

