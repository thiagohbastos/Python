n = int(input('Digite um número: '))
cont = 0

print('Divisores: ', end=' ')
for c in range (1, n + 1):
    if n % c == 0 and c != 1 and c != n:
        cont += 1
        print('{}{}{}'.format('\033[1:31m', c, '\033[m'), end= ' ')
    elif n % c == 0:
        cont += 1
        print('{}{}{}'.format('\033[1:34m', c, '\033[m'), end=' ')
print('\nO número {} foi divisível {} vezes.'.format(n, cont))
if cont >= 3:
    print('Por isso ele NÃO É PRIMO!')
else:
    print('Por isso ele É PRIMO!')