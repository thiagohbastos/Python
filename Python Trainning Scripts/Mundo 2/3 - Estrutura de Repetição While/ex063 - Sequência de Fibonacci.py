r = int(input('Favor informar a quantidade de números da {}sequência de Fibonacci{} desejada: '.format('\033[1:33m', '\033[m')))
n1 = 0
n2 = 1

if r == 1:
    print('{}→{} 0'.format('\033[1:34m', '\033[m'), end='')
elif r == 2:
    for c in range (0, 2, 1):
        print('{}→{} {} '.format('\033[1:34m', '\033[m', c), end='')
elif r <= 0:
    print('Apenas inteiros positivos são aceitos!')
else:
    for c in range (0, 2, 1):
        print('{}→{} {} '.format('\033[1:34m', '\033[m', c), end='')
    cont = 2
    while cont < r:
        soma = n1 + n2
        print('{}→{} {} '.format('\033[1:34m', '\033[m', soma), end='')
        n1 = n2
        n2 = soma
        cont += 1
print('\n----- {}Programa Finalizado{} -----'.format('\033[1:33m','\033[m'))
