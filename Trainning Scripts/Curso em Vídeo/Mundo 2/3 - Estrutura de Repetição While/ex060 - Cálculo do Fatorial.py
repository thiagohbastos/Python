n = abs(int(input('Favor digitar um número inteiro positivo para saber seu fatorial: ')))
n1 = n
f = n
if n == 0:
    print('0! = 1')
    print('O fatorial de 0 é sempre 1!')
if n >= 1:
    print('{}! = {} '.format(n, n), end='')
    while n1 > 1:
        n1 -= 1
        f *= n1
        print('{}x{} {} '.format('\033[1:36m', '\033[m', n1), end='')
    print('= {}'.format(f))
