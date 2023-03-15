frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
# o comando split e o join foram utilizados para retirar os
# espaços internos da palavra
inverso = ''
inverso = junto[::-1] #essa solução tem abse no fatiamento de str
'''for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A frase digitada não é um palindromo!')
