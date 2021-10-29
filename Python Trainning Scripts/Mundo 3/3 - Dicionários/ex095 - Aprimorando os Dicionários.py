jogador = {}
gols, geral = [], []

while True:
    jogador['nome'] = str(input('Nome do Jogador: ')).strip().title()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    for cont in range(0, partidas):
        gols.append(int(input(f'   - Gols marcados na {cont + 1}ª partida: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols[:])
    geral.append(jogador.copy())
    jogador.clear(), gols.clear()
    while True:
        resp = str(input('Gostaria de continuar? [S/N] ')).strip().upper()
        if resp in 'SN':
            break
        print('\033[1:31mOpção inválida!\033[m')
    print('\033[1:33m-\033[m' * 63)
    if resp == 'N':
        break

print('\033[1:34m{:<4}{:<15}{:<15}{:<15}\033[m'.format('CÓD', 'NOME', 'GOLS', 'TOTAL'))
print('-' * 63)
for i, v in enumerate(geral):
    print('{:<4}'.format(i + 1), end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 63)
while True:
    consulta = int(input('Mostrar dados de qual jogador? (0 para parar) '))
    if consulta == 0:
        break
    if consulta not in range (1, len(geral) + 1):
        print(f'\033[1:31mERRO! Não há jogador com o código {consulta}. \033[m')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {geral[consulta - 1]["nome"].upper()} -- ')
        for i, v in enumerate(geral[consulta - 1]["gols"]):
            print(f'       No jogo {i + 1} fez {v} gols.')
    print('-' * 63)
print('<<< VOLTE SEMPRE >>>')