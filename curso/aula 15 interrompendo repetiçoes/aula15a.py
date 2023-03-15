#while true executa a etrutura infinitamente, onde so pode
# ser parada com o comando break
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
# print('A soma vale {}'.format(s))
print(f'A soma vale {s}')
nome = 'josé'
idade = 33
salário = 987.3
print(f' o {nome} tem {idade} anos e ganha R${salário:.2f}')
