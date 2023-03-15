print('=' * 50)
print(' ' * 15,  'LISTAGEM DE PREÇOS')
print('=' * 50)
produto = 'lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,\
    'Mochila', 120.32, 'Caneta', 22.30, 'Livro', 34.90
for n in range(0, 18, 2):
    print(f'{produto[n]:.<40} R$ {produto[n + 1]}')
print('=' * 50)
