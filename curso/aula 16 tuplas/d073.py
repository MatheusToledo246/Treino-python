brasileirao = 'corinthans', 'palmeiras', 'santos', 'gremio','cruzeiro', 'flamengo', 'vasco', 'chapecoense',\
    'atletico-mg', 'botafogo', 'atletico-pr', 'bahia', 'são paulo', 'fluminense', 'sport', 'vitoria', 'coritiba',\
    'avai', 'ponte preta', 'atletico-go'
print(f'Os 5 primeiros colocados são {brasileirao[0:5]}')
print(f'Os 4 ultimos colcoados são {brasileirao[-4:]}')
print(f'Ordem alfabetica: {sorted(brasileirao)}')
print(f'A chapeconese está na posição {brasileirao.index("chapecoense")+1}ª posição')
#pro index funcinar deve utilizar aspas duplas.
