#Crie um programa que tenha uma tupla única com nomes
# de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando
# os dados em forma tabular.
print('=' * 40)
print(' '*10, 'LISTAGEM DE PREÇOS')
print('=' * 40)
produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.00, 'Estojo', 25.00,
            'Transferidos', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30,
            'Livro', 34.90)
for n in range(0, len(produtos), 2):
    print(f'{produtos[n]:.<30} RS{produtos[n+1]:>7.2f}')
print('=' * 40)
