n = int(input('Favor digitar um número para exibição de sua tabuada: '))
cont = 1
print('A tabuada de {} é: '.format(n))
print('-' * 12)
while cont < 11:
    print('{:2} * {:2} = {}'.format(n, cont, n * cont))
    cont = cont + 1
print('-' * 12)
