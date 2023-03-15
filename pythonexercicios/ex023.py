# leia um numero de 0-9999 e mostre os digitos separados
n = int(input('Informe um numero: '))
u = (n // 1) % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

# a quantidade de 0 depois do % 1 indica quantos
# numeros vc quer que apareça