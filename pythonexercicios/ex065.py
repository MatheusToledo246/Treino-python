#Crie um programa que leia vários números inteiros
# pelo teclado. No final da execução, mostre a média
# entre todos os valores e qual foi o maior e o menor
# valores lidos. O programa deve perguntar ao usuário
# se ele quer ou não continuar a digitar valores.
ct = 'S'
media = menor = maior = cont = 0
while ct not in 'N':
    n = int(input('Digite um número: '))
    ct = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    media += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

print('Você digitou {} Números e a média foi {:.2f}'.format(cont, media/cont))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
