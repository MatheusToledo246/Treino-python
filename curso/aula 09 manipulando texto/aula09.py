# o python diferencia maiuscula de minuscula
# se colocar frase = [9:13] ele vai pegar de 9 até 12
# frase = [9:13:2] faz o arquivo pular de 2 em dois numeros
# quando nao se coloca numero inicial frase = [:5] ele começa do 0
# se indicar o inicio frase = [15:] ele vai do  15 até o final
# frase = [9::3] começa do nove e vai até o final pulando de 3 em 3
# analise de string
#len(frase) ele conta quantas letras tem no nome(com espaços).
#frase.count {'o'} ele conta quantavs vezes aparece a letra o minusculo
#frase.count('o',0,13) vai contar as letras o do 0 e o 12
#frase.find('deo') quantas vezes ele encontrou deo(ele vai indicar que comemnto começou)
#se vc colcoar uma palavra que não exita no find ele te da o valor -1
# o operador in indica se exite ou nao a palvra dentro da string
# exemplo do operador in ('curso' in frase).
# transformação de string
# frase.replace('python','android') ele procura a palvra python
#e subistitui pela palavra android.
# frase.upper() esse método faz com que as letras minusculas virem amisculas
# frase.lower() troca as letras maiusculas por minusculas.
#frase.capitalize() joga tudo pra minusculo e a primeira letra fica maiuscula
# frase.title() ele analisa as primeiras letras depois do espaço em amiusculas
# frase.trip() tira todos os espaços inuteis da string
# frase.rstrip() tiras os espaços da direita.
# frase.lstrip() tira os espaços da esquerda.
# frase.split() divide onde esta os espaços da string(divide ums string em listas)
# '-'.join(frase) ele junta as lista em uma string novemnte com um - separando as palavras.
# " ".join(frase) ele junta com um espaço separando as palavras novamente.