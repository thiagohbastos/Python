valores, p_5 = list(), list()
while True:
    v = int(input('Digite um valor: '))
    valores.append(v)
    if v == 5:
        p_5.append(len(valores))
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
        if resp in 'SN':
            break
    if resp == 'N':
        break
print('-='*25)
print(f'Você digitou {len(valores)} elementos.')
print('Os valores em órdem decrescente são {}'.format(sorted(valores, reverse=True)))
if valores.count(5) == 0:
    print('O valor 5 não faz parte da lista!')
else:
    print('O valor 5 faz parte da lista e foi digitado {} {}'.format('nas posições' if valores.count(5) > 1
                                                                     else 'na posição', p_5))