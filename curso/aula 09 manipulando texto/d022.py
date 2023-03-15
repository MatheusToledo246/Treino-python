p = str(input('Digite seu nome completo: ')).strip()
print('seu nome com letras maiusuclas é: {}'.format(p.upper()))
print('Seu nome com letras minusculas é: {}'.format(p.lower()))
print('seu nome tem {} letras'.format(len(p)-p.count(' ')))
print('Seu primeiro nome tem {} letras'.format(p.find(' ')))
#o strip no começo tira os espaços inuteis
#.format(len(p)-p.count(' '))) serve pra tirar os epaços restantes
