print('{}{}{}'.format('\033[1;33m', '='*40, '\033[m'))
print('{}{: ^40}{}'.format('\033[1m', '10 TERMOS DE UMA PA (ou mais)', '\033[m'))
print('{}{}{}'.format('\033[1;33m', '='*40, '\033[m'))

n1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
cont = 0

while cont <= 9:
    print('{} {}→ {}'.format(n1 + cont * r, '\033[1:35m', '\033[m'), end='')
    cont += 1
print('\033[1:33mITs OVER!\033[m')

mais = int(input('{}Gostaria de mostrar mais quantos termos desta P.A.? (digite 0 para finalizar) {}'.format('\033[1m', '\033[m')))
while mais != 0:
    if mais < 0:
        print('{}Favor digitar um número positivo!{}'.format('\033[1:31m', '\033[m'))
    else:
        suporte = cont - 1
        while cont <= suporte + mais:
            print('{} {}→ {}'.format(n1 + cont * r, '\033[1:35m', '\033[m'), end='')
            cont += 1
        print('\033[1:33mITs OVER!\033[m')
    mais = int(input('{}Gostaria de mostrar mais quantos termos desta P.A.? (digite 0 para finalizar) {}'.format('\033[1m', '\033[m')))
print('Progressão Aritimética finalizada com {} termos mostrados.'.format(cont))