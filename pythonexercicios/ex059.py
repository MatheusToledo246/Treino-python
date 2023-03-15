#''' Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa'''
n = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
menu = 0
while menu != 5:
    print(''' === MENU ===
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    menu = int(input('Qual sau opção? '))
    if menu == 1:
        print('{} + {} = {}'.format(n, n2, n+n2))
    elif menu == 2:
        print('{} X {} = {}'.format(n, n2, n * n2))
    elif menu == 3:
        if n > n2:
            print('{} é maior que {}'.format(n, n2))
        elif n2 > n:
            print('{} é maior que {}'.format(n2, n))
    elif menu == 4:
        n = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif menu == 5:
        print('Finalizando...')
    else:
        print('opção invalida, tente novamente...')
