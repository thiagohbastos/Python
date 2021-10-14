lista = list()
for cont1 in range (0, 5):
    v = int(input('Digite um valor: '))
    print('Adicionado ', end='')
    if cont1 == 0 or v > max(lista):
        lista.append(v)
        print('ao final ', end='')
    else:
        pos = 0
        while True:
            if v <= lista[pos]:
                lista.insert(pos, v)
                print(f'na posição {pos} ', end='')
                break
            pos += 1
    print('da lista.')
print('-='*25)
print(f'Os valores digitados em órdem foram {lista}')