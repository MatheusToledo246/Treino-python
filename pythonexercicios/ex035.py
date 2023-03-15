# leia 3 segmenyos(retas) e diga se podem formar um triangulo
print('-=' * 20)
print('Analisador de Triângulos!!!')
print('-=' * 20)
n = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if (n + n2) > n3 and (n + n3) > n2 and (n2 + n3) > n:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
