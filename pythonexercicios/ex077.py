#Crie um programa que tenha uma tupla com várias palavras
# (não usar acentos). Depois disso, você deve mostrar,
# para cada palavra, quais são as suas vogais.
palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:#analisa todos os elementos da tupla
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:# para cada letra na palavra (p)
        if letra.lower() in 'aeiou':#selecionar as vogais aeiou
            print(letra, end=' ')
