s = 0
cont = 0
for c in range (0, 501, 3):
    if c % 3 == 0 and c % 2 != 0:
        cont += 1
        s += c
print('A soma de todos os {} valores solicitados é {}.'.format(cont, s))