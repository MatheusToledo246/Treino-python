# Crie um programa que leia uma frase qualquer e
# diga se ela é um palíndromo, desconsiderando os espaços.
frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A frase digitada não é um palíndromo!')
#o ''.join(palavras) serve pra juntar as lavras tirando
# todos os espaços do meio
# o len(junto) - 1 serve pra ler a frase de tras pra frente.