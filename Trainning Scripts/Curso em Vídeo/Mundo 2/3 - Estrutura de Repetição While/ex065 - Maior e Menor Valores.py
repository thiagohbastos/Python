cont = s = 0
r = 'S'

while r == 'S':
    n = float(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
    cont += 1
    s += n
    if cont == 1:
        maior = menor = s = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    while r not in 'SN':
        print('{}Favor digitar uma resposta válida!{}'.format('\033[1:31m', '\033[m'))
        r = str(input('Quer continuar? {}[S/N]{} '.format('\033[1:31m', '\033[m'))).strip().upper()

print('Você digitou {} números e a média deles foi {:.2f}.'.format(cont, s/cont))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
