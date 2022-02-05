valores, p_maiores, p_menores = list(), list(), list()
print('Digite 5 números inteiros:')
for c in range(1, 6):
    valores.append(int(input(f'{c}ª posição - ')))
for c, valor in enumerate(valores):
    if valor == max(valores):
        p_maiores.append(c + 1)
    elif valor == min(valores):
        p_menores.append(c + 1)
print('\033[1:34m=-\033[m'*25)
print(f'Você digitou os valores {valores}')
print('O maior valor digitado foi {} {} {}.'.format(max(valores),
                                                    "na posição" if valores.count(max(valores)) == 1
                                                    else "nas posições",
                                                    p_maiores))
print('O menor valor digitado foi {} {} {}.'.format(min(valores),
                                                    "na posição" if valores.count(min(valores)) == 1
                                                    else "nas posições",
                                                    p_menores))
