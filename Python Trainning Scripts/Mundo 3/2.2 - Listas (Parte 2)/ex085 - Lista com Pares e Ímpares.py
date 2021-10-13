lista = [[], []]

for cont1 in range (1, 8):
    v = int(input(f'Digite o {cont1}º valor: '))
    if v % 2 == 0:
        lista[0].append(v)
    else:
        lista[1].append(v)
lista[0].sort()
lista[1].sort()

print('-'*40)
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores ímpares digitados foram: {lista[1]}')