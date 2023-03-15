# indque o angulo e decubra, seno, cosseno e tangente
from math import sin, cos, tan, radians
n = float(input('Digite o ângulo que você deseja: '))
print('O ângulo de {} tem o SENO de {:.2f}'.format(n, sin(radians(n))))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(n, cos(radians(n))))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(n, tan(radians(n))))
#pra calcular os angulos o valor deve estar em radianos