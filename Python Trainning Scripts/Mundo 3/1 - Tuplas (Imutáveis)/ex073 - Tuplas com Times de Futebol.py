tabela = 'Atlético Mg',	'Palmeiras', 'Fortaleza', 'Flamengo', 'Bragantino', 'Corinthians', 'Internacional', 'Fluminense',	\
         'Athletico Pr', 'Cuiabá', 'Ceará',	'Atlético Go', 'São Paulo',	'Juventude', 'América-MG', 'Santos', 'Bahia',\
         'Grêmio', 'Sport', 'Chapecoense'
print('Os cinco primeiros colocados: ')
print(f'\033[1:32m{tabela[0:6]}\033[m\n')

print('Os quatro na zona de rebaixamento: ')
print(f'\033[1:31m{tabela[-4:]}\033[m\n')

print('Todos os times em órdem alfabética: ')
print(sorted(tabela), end='.\n\n')

print('-'*80)
while True:
    time = str(input('Favor digitar um outro time para saber sua posição (favor digitar como demonstrado acima): ')).strip().title()
    print('-' * 80)
    if tabela.count(time) != 0:
        print(f'O {time} está atualmente na {tabela.index(time) + 1}ª posição!')
    else:
        print('O time informado não existe, foi digitado incorretamente ou não se encontra na série A!')
    resp = str(input('Gostaria de verificar outro time? [S/N] ')).strip().upper()
    while resp not in 'SN':
        resp = str(input('Gostaria de verificar outro time? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print('\n{:=^80}'.format(' PROGRAMA FINALIZADO '))
