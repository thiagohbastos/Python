print('{}{}{}'.format('\033[1;33m', '='*40, '\033[m'))
print('{}{: ^40}{}'.format('\033[1m', '10 TERMOS DE UMA PA', '\033[m'))
print('{}{}{}'.format('\033[1;33m', '='*40, '\033[m'))

n1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))

for c in range (0, 10):
    print('{} '.format(n1 + r * c), end = '→ ')
print('ITs OVER!')