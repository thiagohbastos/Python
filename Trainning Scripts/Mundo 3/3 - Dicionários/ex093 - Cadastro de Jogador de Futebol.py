cadastro_jogador = {}
gols = []

cadastro_jogador['nome'] = str(input('Nome do Jogador: ')).strip().title()
partidas = int(input(f'Quantas partidas {cadastro_jogador["nome"]} jogou: '))

for cont in range(0, partidas):
    gols.append(int(input(f'   - Gols marcados na {cont + 1}ª partida: ')))
cadastro_jogador['gols'] = gols[:]
cadastro_jogador['total'] = sum(gols[:])

print('\033[1:33m-\033[m'*60)
print(cadastro_jogador)

print('\033[1:33m-\033[m'*60)
for k, v in cadastro_jogador.items():
    print(f'O campo {k.capitalize()} tem o valor {v}.')

print('\033[1:33m-\033[m'*60)
print(f'O jogador {cadastro_jogador["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(cadastro_jogador['gols']):
    print(f'   - Na {i + 1}ª partida fez {v} gols.')
print(f'Em resumo, o jogador {cadastro_jogador["nome"]} fez {cadastro_jogador["total"]} gols em '
      f'{len(cadastro_jogador["gols"])} jogos.')
