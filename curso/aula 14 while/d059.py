n = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
calc = 0
while calc != 5:
    calc = int(input('''
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos numeros
[ 5 ] Sair
Escolha um valor: '''))
    if calc == 1:
        print('{} + {} = {}'.format(n, n2, n + n2))
    elif calc == 2:
        print('{} X {} = {}'.format(n, n2, n * n2))
    elif calc == 3:
        if n > n2:
            print('{} é maior que {}'.format(n, n2))
        else:
            print('{} é maior que {}'.format(n2, n))
    elif calc == 4:
        print('Informe os numeros novamente: ')
        n = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif calc == 5:
        print('Finalizando...')
    else:
        print('Opção invalida, tente novamente')
