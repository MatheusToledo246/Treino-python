# crie um conversor de inteiro para as 3 bases
# binario, octal e hexadecimal
n = int(input("digite um número inteiro: "))
#bs = int(input('Escolha uma das bases para conversão: '
              # '\n[ 1 ] Converter para BINÁRIO'
              #'\n[ 2 ] Converter para OCTAL'
              # '\n[ 3 ] Converter para HEXADECIMAL'
              #'\nSua opção: '))
bs = int(input('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL
Sua opção: '''))
#para colcoar mais linhas pode se usar ''' tres áspas no input
if bs == 1:
    print('{} Convertido para BINÁRIO é igual á {}'.format(n, bin(n)[2:]))
    #colocar o [2:] nofinal faz com que pule o simbolo de binario
    #que o python deixa ao calcular o valor
elif bs == 2:
    print('{} Convertido para OCTAL é igual á {}'.format(n, oct(n)[2:]))
elif bs == 3:
    print('{} Convertido para HEXADECIMAL é igual á {}'.format(n, hex(n)[2:]))
else:
    print('ERRO! Opção invalida.')
