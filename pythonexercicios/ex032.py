# indique se o ano é bissexto
from datetime import date #biblioteca para comandos de datas
a = int(input('Que ano vc quer analisar? coloque 0 para ano atual: '))
if a == 0:
    a = date.today().year # comando pra executar o ano atual
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('O ano {} é BISSEXTO!!!'.format(a))
else:
    print('O ano {} NÃO é BISSEXTO!!!'.format(a))
