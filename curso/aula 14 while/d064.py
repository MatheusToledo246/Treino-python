n = int(input('Digite um número:'))
qn = 0
soma = 0
while n != 999:
    qn += 1
    soma += n
    print('Para encerrar digite 999.')
    n = int(input('Digite um número:'))
print('Foram digitados {} numeros'.format(qn))
print('A soma de todos os números digitados é {}'.format(soma))