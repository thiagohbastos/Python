print('{}{}{}'.format('\033[1;40m', '-=-'*13, '\033[m'))
print('{}{: ^39}{}'.format('\033[1;35m', 'GAME: Pedra, Papel e Tesoura', '\033[m'))
print('{}{}{}'.format('\033[1;40m', '-=-'*13, '\033[m'))

from random import choice
from time import sleep

print('Para iniciar, vou escolher entre pedra, papel e tesoura!')
d = choice(['PEDRA', 'PAPEL', 'TESOURA'])

sleep(3)

u = str(input('''Prontinho! Já sei o que vou querer!
Vamos lá? Qual sua escolha? ''')).strip().upper()

if u in 'PEDRA, PAPEL e TESOURA':
    sleep(0.5)
    print('JO ', end = '')
    sleep(0.5)
    print('KEN ', end = '')
    sleep(0.5)
    print('PO!')

    if d == u:
        print('Vishe! Deu {}EMPATE{}!'.format('\033[1:33m', '\033[m'))
    elif d == 'PEDRA' and u == 'TESOURA' or d == 'TESOURA' and u == 'PAPEL' or d == 'PAPEL' and u == 'PEDRA':
        print('{}HAHAHA Eu escolhi {}! {} ganha de {}!'.format('\033[1:31m', d, d, u))
    else:
        print('{}Poxa... Eu escolhi {}! {} ganha de {}! Você ganhou :('.format('\033[1:32m', d, u, d))
else:
    print('{}ACHEI QUE VOCÊ QUISESSE JOGAR. Escolha uma opção válida né...'.format('\033[1:34m', d, u, d))