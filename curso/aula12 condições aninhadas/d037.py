n = int(input('Digite um numéro para a conversão: '))
b = int(input('Escolha uma base para á conversão '
              '\n[ 1 ] para Binário \n[ 2 ] para Octal '
              '\n[ 3 ]para Hexadecimal'
              ' \nQual á base de conversão: '))
if b == 1:
    print('{} convertido para Binário é igual á {}'.format(n, bin(n)[2:]))
elif b == 2:
    print('{} convertido para Octal é igual á {}'.format(n, oct(n)[2:]))
elif b == 3:
    print('{} convertido para Hexadecimal é igual á {}'.format(n, hex(n)[2:]))
else:
    print('erro, numero não identificado!')

