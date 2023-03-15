# converta um nome em maiusculo, minusculo e quantras letras
# ele tem e qauntas lertas tem o primeiro nome
p = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(p.upper()))
print("Seu nome em minúsculas é {}".format(p.lower()))
print('Seu nome tem ao todo {} letras'.format(len(p)-p.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(p.find(' ')))
separa = p.split()
print('Seu primeiro nome tem {} letras'.format(len(separa[0])))
# realizando o len(p)-p.count(' ') é possivel tirar o espaço
# que fica entre as palavras
# o p.find(' ') conta quantos caracteres tem antes do primeiro
# espaço