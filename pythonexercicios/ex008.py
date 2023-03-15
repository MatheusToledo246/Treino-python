# converta a distancia de metros para centimetros e milimetros
n = float(input('Digite a distância em metros: '))
#c = n * 100
#m = n * 1000
#print('{} metros é igual á {:.2f} centimetros \n{} metros é igual á {:.2f} milimetros.'.format(n, c, n, m))
print('{} metros é igual á {} centimetros'.format(n, (n * 100)))
print('{} metros é igual á {} milimetros'.format(n, (n * 1000)))