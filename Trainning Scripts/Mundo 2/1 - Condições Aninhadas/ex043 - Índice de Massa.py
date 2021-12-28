print('{}{}{}'.format('\033[1;40m', '-=-'*13, '\033[m'))
print('{}{: ^39}{}'.format('\033[1;31m', 'Índice de Massa', '\033[m'))
print('{}{}{}'.format('\033[1;40m', '-=-'*13, '\033[m'))

p = float(input('Qual seu peso? (Kg) '))
a = float(input('E qual a sua altura? (m) '))
imc = p / (a**2)

print('Seu IMC é {:.1f}.'.format(imc))

if imc < 18.5:
    print('Você está {}ABAIXO DO PESO{}.'.format('\033[1:31m', '\033[m'))
elif imc < 25:
    print('Você está no {}PESO IDEAL{}.'.format('\033[1:32m', '\033[m'))
elif imc < 30:
    print('Você está na faixa de {}SOBREPESO{}.'.format('\033[1:31m', '\033[m'))
elif imc < 40:
    print('Você está com{}OBESIDADE{}'.format('\033[1:31m', '\033[m'))
else:
    print('Você está com {}OBESIDADE MÓRBIDA{}.'.format('\033[1:31m', '\033[m'))