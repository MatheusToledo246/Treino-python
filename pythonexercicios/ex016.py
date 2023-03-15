# indicar qual a porção inteira de um numero real
#import math
from math import trunc
n = float(input('Digite um número Real: '))
print('A porção inteira de {} é igual á {}'.format(n, trunc(n)))
#print('A porção interia de {} é igual á {}ma'.fort(n, math.floor(n)))
# se utilizar o trunc ela corta o valor pra deixar so o valor real