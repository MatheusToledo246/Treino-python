# principakl diferença entre for e while é que no
# for vc precisa dar um limite de repetições para a estrutura.
#for: quando se sabe o limite de repetições por é mais pratico
#while: quando não se sabe o limite de repetições.
#While: estrutura de repetição com teste lógico.
'''for c in range(1,10):
    print(c)
print('Fim')'''
#quando se sabe o limite
'''c = 1
while c < 10:
    print(c)
    c = c + 1
print('fim')'''
#quando se sabe o limite
'''for c in range(1, 5):
    n = int(input('Digite umv valor: '))
print('Fim')'''
'''n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')'''
#qundo não tem limite.
'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]')).upper()
print('Fim')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Voce digitou {} números pares e {} numeros impares'.format(par, impar))
