p = float(input('Qual o seu peso? '))
a = float(input('Qual á sua altura? '))
imc = p / (a*a)
if imc < 18.5:
    print('Seu IMC é {:.2f} e vc está a baixo do péso.'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é {:.2f} e vc está no Peso ideal.'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é {:.2f} e vc está com Sobrepeso.'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é {:.2f} e vc está com Obesidade.'.format(imc))
else:
    print('Seum IMC é {:.2f} e vc está com Obesidade Mórbida.'.format(imc))
