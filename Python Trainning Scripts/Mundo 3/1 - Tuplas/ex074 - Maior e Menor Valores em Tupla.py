from random import randint
tupla = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
print('Os valores sorteados foram: ', end='')
for n in tupla:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi {sorted(tupla)[4]}')
print(f'O menor valor sorteado foi {sorted(tupla)[0]}')