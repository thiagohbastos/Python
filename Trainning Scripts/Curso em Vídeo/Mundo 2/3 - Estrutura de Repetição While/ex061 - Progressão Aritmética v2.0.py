print('{}{}{}'.format('\033[1;33m', '='*40, '\033[m'))
print('{}{: ^40}{}'.format('\033[1m', '10 TERMOS DE UMA PA', '\033[m'))
print('{}{}{}'.format('\033[1;33m', '='*40, '\033[m'))

n1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
cont = 0

while cont <= 9:
    print('{} {}→ {}'.format(n1 + cont * r, '\033[1:35m', '\033[m'), end='')
    cont += 1
print('\033[1:33mITs OVER!\033[m')