#Melhore o DESAFIO 061, perguntando para o usuário
# se ele quer mostrar mais alguns termos. O programa
# encerrará quando ele disser que quer mostrar 0 termos.
print('Gerador de PA')
print('-=' * 10)
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = n
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += r
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} temos mostrados'.format(total))