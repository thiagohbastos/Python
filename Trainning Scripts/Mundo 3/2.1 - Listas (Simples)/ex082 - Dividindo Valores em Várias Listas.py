original = list()
while True:
    original.append(int(input('Digite um valor: ')))
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
        if resp in 'SN':
            break
    if resp == 'N':
        break

impares = original[:]
c = 0
while c < len(impares):
    if impares[c] % 2 == 0:
        del impares[c]
    else:
        c += 1

pares = original[:]
c = 0
while c < len(pares):
    if pares[c] % 2 != 0:
        del pares[c]
    else:
        c += 1

print('-='*25)
print(f'Os valores digitados foram {original}')
print(f'Os valores ímpares: {sorted(impares)}')
print(f'Os valores pares: {sorted(pares)}')