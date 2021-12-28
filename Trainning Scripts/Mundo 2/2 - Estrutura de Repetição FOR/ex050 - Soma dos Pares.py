s = 0
cont = 0
for c in range (1, 7):
    n = int(input('Favor digitar o {}º número: '.format(c)))
    if n % 2 == 00:
        s += n
        cont += 1
print('A soma de todos os {} números pares informados é {}{}{}!'.format(cont, '\033[1:34m', s, '\033[m'))