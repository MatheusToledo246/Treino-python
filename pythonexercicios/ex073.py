#Crie uma tupla preenchida com os 20 primeiros colocados
# da Tabela do Campeonato Brasileiro de Futebol, na ordem
# de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.

times = 'Corinthans', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético-mg',\
    'Botafogo', 'Atlético-pr', 'Bahia', 'São Paulo', 'Fluminense', 'Sport', 'Vitória', 'Coritiba', 'Avaí', \
    'Ponte Preta', 'Atlético-go'
print(f'Times: {times}')
print('=-' * 20)
print(f'5 primeiros colocados: {times[:5]}')
print('=-' * 20)
print(f'4 ultimos colocados: {times[-4:]}')
print('=-' * 20)
print(f'Ordem alfabética: {sorted(times)}') #comando sorted deixa a lista em ordem alfabetica.
print('=-' * 20)
print(f'A Chapecoense está na posição : {times.index("Chapecoense") + 1}ª') #deve sempre utilizar aspas dupla no index
