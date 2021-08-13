n = int(input('Favor digitar um número para exibição de sua tabuada: '))
cont = 1
print('A tabuada de {} é: '.format(n))
while cont < 11:
    print('{} * {} = {}'.format(n, cont, n * cont))
    cont = cont + 1
