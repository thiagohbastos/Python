from random import randint
from time import sleep
jogo_atual = []

print('{}-{}'.format('\033[1:30m', '\033[m')*40)
print('\033[1:36m{: ^40}\033[m'.format('JOGO NA MEGA SENA'))
print('{}-{}'.format('\033[1:30m', '\033[m')*40)

jogos = int(input('Quantos jogos quer que eu sorteie? '))
print('\033[1:36m{:=^40}\033[m'.format(f' SORTEANDO {jogos} JOGOS '))
for cont1 in range (1, jogos + 1):
    sleep(1)
    for cont2 in range (0, 7):
        while True:
            elemento = randint(1, 60)
            if elemento not in jogo_atual:
                jogo_atual.append(elemento)
                break
    jogo_atual.sort()
    print(f'Jogo {cont1}: {jogo_atual}')
    jogo_atual.clear()
sleep(1)
print('\033[1:36m{:=^40}\033[m'.format(' BOA SORTE! '))
