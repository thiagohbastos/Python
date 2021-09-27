from random import randint

print('{}-={}'.format('\033[1;34m', '\033[m') * 20)
print('{: ^40}'.format('VAMOS JOGAR PAR OU ÍMPAR'))
print('{}-={}'.format('\033[1;34m', '\033[m') * 20)

vitorias = 0

while True:
    comp = randint(1, 10)
    player = int(input('Digite um valor: '))
    pí = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    while pí not in 'PI':
        print('{}Digite apenas P ou I por gentileza!{}'.format('\033[1:31m', '\033[m'))
        pí = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    if (comp + player) % 2 == 0 and pí == 'I' or (comp + player) % 2 != 0 and pí == 'P':
        print('{}-{}'.format('\033[1;34m', '\033[m') * 40)
        print('Você jogou {} e o computador {}. O total foi {} que é {}'.format(player, comp, comp + player,'par.' if pí == 'I' else 'ímpar.'))
        break
    vitorias += 1
    print('{}-{}'.format('\033[1;34m', '\033[m') * 40)
    print('Você jogou {} e o computador {}. O total foi {} que é {}'.format(player, comp, comp + player, 'par.' if pí == 'P' else 'ímpar.'))
    print('{: ^40}'.format('VOCÊ GANHOU! Vamos jogar novamente...'))
    print('{}-{}'.format('\033[1;34m', '\033[m') * 40)
print('{: ^40}'.format('VOCÊ PERDEU!'))
print('{}-={}'.format('\033[1;34m', '\033[m') * 20)
print(f'GAME OVER! Você venceu {vitorias} vezes.')
