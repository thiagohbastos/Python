cadastro, auxiliar, pesos = list(), list(), list()

while True:
    auxiliar.append(str(input('Nome: ')).strip().title())
    auxiliar.append(float(input('Peso: ')))
    cadastro.append(auxiliar[:])
    pesos.append(cadastro[-1][-1])
    auxiliar.clear()
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
        if resp in 'SN' and resp != '':
            break
    if resp == 'N':
        break
    print('\033[1:33m---\033[m'*15)
print('\033[1:33m-=-\033[m'*20)

n = len(cadastro)
maior = max(pesos)
menor = min(pesos)
print(f'Ao todo você cadastrou {n} {"pessoas" if n > 1 else "pessoa"}.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in cadastro:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')
for p in cadastro:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
