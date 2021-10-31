def área(l, c):
    a = l * c
    print(f'A área de um terreno {l:.1f}m x {c:.1f}m é de {a:.1f}m²')


print('-' * 40)
print('{:^40}'.format('Controle de Terrenos'))
print('-' * 40)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)
