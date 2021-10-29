from random import randint
from time import sleep
from operator import itemgetter

resultado, ranking = {}, list()

print('Valores sorteados:')
for n in range(1, 5):
    resultado[f'jogador {n}'] = randint(1, 6)
for k, v in resultado.items():
    sleep(1)
    print(f'O {k} tirou {v}.')
ranking = sorted(resultado.items(), key=itemgetter(1), reverse=True)

print('{}{:=^30}{}'.format('\033[1:36m', ' RANKING DOS JOGADORES ', '\033[m'))
sleep(1)
for i, v in enumerate(ranking):
    sleep(1)
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}.')
