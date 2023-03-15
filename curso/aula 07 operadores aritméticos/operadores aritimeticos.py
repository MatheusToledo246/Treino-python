n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
d2 = n1 // n2
e = n1 ** n2
print('A soma vale {}, \n o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}'.format(d2, e))
# colocar o :.3f dentro da chave faz com que apareça somente 3 casas após a virgula
# pra não quebrar a linha é so adicionar ,end=' ' depois do format
# pra separar o mesmo print em várias linhas é so adicionar \n