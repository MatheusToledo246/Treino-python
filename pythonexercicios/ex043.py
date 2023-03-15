#calcule o imc e indique o pesod a pesoa, abaixo do peso
# imc menor que 18.5, entre 18.5 e 25 peso normal,
# entre 25 e 30 sobrepeso, entre 30 e 40 obesidade
# e acima de 40 obesidade morbida.
kg = float(input('Peso(Kg): '))
al = float(input('Altura(metros): '))
imc = kg / (al ** 2)
print('O IMC dessa pesoa é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você esá ABAIXO DO PESO NORMAL!')
elif 18.5 <= imc < 25:
    print('PARABÉNS,Você esta no PESO NORMAL!')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO!')
elif 30 <= imc < 40:
    print('Você está com OBESIDADE!')
else:
    print('Você está com OBESIDADE MÓRBIDA, cuidado!')
