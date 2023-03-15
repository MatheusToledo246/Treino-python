#Desenvolva um programa que leia o primeiro termo
# e a razão de uma PA. No final, mostre os 10
# primeiros termos dessa progressão.
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a Razão: '))
decimo = termo + (10 - 1) * razao
print('=' * 40)
print('     10 TERMOS DE UMA PA  ')
print('=' * 40)
print('Primeiro Termo: {}'.format(termo))
print('Razão: {}'.format(razao))
for c in range(termo, decimo + razao, razao):
    print(c, end=' -> ')
print('ACABOU!')
