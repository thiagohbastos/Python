tabela = 'Atlético Mg',	'Palmeiras', 'Fortaleza', 'Flamengo', 'Bragantino', 'Corinthians', 'Internacional', 'Fluminense',	\
         'Athletico Pr', 'Cuiabá', 'Ceará',	'Atlético Go', 'São Paulo',	'Juventude', 'América-MG', 'Santos', 'Bahia',\
         'Grêmio', 'Sport', 'Chapecoense'
print('Os cinco primeiros colocados: ')
for melhores in range(0, 5):
    print(f'\033[1:32m{melhores + 1}º\033[m - {tabela[melhores]}')

print('Os quatro na zona de rebaixamento: ')
for piores in range(-4, 0, 1):
       print(f'\033[1:31m{tabela.index(tabela[piores]) + 1}º\033[m - {tabela[piores]}')

print('Todos os times em órdem alfabética: ')
for cont in range (0, len(tabela), 1):
    if cont != 19:
        print(sorted(tabela)[cont], end=', ')
    else:
        print(sorted(tabela)[cont], end='.\n\n')
print('-'*80)
while True:
    time = str(input('Favor digitar um outro time para saber sua posição (favor usar acentuação): ')).strip().title()
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