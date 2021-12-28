print('{}{}{}'.format('\033[1;40m', '-=-'*13, '\033[m'))
print('{}{: ^39}{}'.format('\033[1;33m', 'Comparando Números', '\033[m'))
print('{}{}{}'.format('\033[1;40m', '-=-'*13, '\033[m'))

n1 = float(input('Favor digitar doi números para comparação: \nPrimeiro número: '))
n2 = float(input('Segundo número: '))
l = [n1, n2]
l.sort()
if n1 == n2:
    print('Não existe valor maior, os dois são iguais.')
elif l[1] == n1:
    print('O primeiro valor é o maior. Ou seja, {} é maior que {}.'.format(n1, n2))
else:
    print('O segundo valor é o maior. Ou seja, {} é maior que {}.'.format(n2, n1))