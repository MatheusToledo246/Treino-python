from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 7+1):
    ano = int(input('Qual seu ano de nascimento? '))
    if atual - ano > 18:
        maior += 1
    else:
        menor += 1
print('{} Pessoas atingiram a maioridade'.format(maior))
print('{} Pessoas não atingiram a maioridade'.format(menor))


