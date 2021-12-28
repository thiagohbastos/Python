def ficha(jogador='<desconhecido>', qtd_gols=0):
    print(f'O jogador {jogador} fez {qtd_gols} gol(s) no campeonato.')


nome = str(input('Nome do jogador: ')).strip().title()
gols = str(input('Número de Gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(qtd_gols=gols)
else:
    ficha(nome, gols)
