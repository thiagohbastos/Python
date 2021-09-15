print('{}{}{}'.format('\033[1;40m', '-=-'*13, '\033[m'))
print('{}{: ^39}{}'.format('\033[1;37m', 'Analisando Triângulos V2.0', '\033[m'))
print('{}{}{}'.format('\033[1;40m', '-=-'*13, '\033[m'))

print('Vamos analisar um triângulo! ')
l1 = float(input('Favor informar o tamanho do primeiro lado: '))
l2 = float(input('Agora, o tamanho do segundo lado: '))
l3 = float(input('Por fim, o terceiro lado: '))

l = [l1, l2, l3]
l.sort()

if l[2] >= (l[0] + l[1]):
    print('{}Não é possível formar um triângulo com os lados {:.0f}, {:.0f} e {:.0f}.{}'.format('\033[1:31m', l[0], l[1], l[2], '\033[m'))
elif l1 == l2 == l3:
    print('O triângulo de todos os lados {:.0f} é {}EQUILÁTERO{}.'.format(l1, '\033[1:34m', '\033[m'))
elif l[0] == l[1] and l[0] != l[2] or l[2] == l[1] and l[0] != l[2]:
    print('O triângulo de dois lados {:.0f} e um lado {:.0f} é {}ISÓSCELES{}.'.format(l[0], l[2], '\033[1:34m', '\033[m'))
else:
    print('O triângulo com todos os lados diferentes é {}ESCALENO{}.'.format('\033[1:34m', '\033[m'))