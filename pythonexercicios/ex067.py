#Faça um programa que mostre a tabuada de vários
# números, um de cada vez, para cada valor digitado
# pelo usuário. O programa será interrompido quando
# o número solicitado for negativo.
#cont = 1
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 20)
    if n < 0:
        break
   # while cont <= 10:
       # print(f'{n} X {cont} = {n * cont}')
       # cont += 1
    for c in range(1,11):
        print(f'{n} X {c} = {n * c}')
    print('-' * 20)
    #cont = 1
print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')
#aelm do while pode se utilizar o for tambem