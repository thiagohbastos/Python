tupla = (int(input('Favor digitar o 1º número: ')),
      int(input('Favor digitar o 2º número: ')),
      int(input('Favor digitar o 3º número: ')),
      int(input('Favor digitar o 4º número: ')))

print(f'\nVocê digitou os valores {tupla}\n')
print(f'O valor 9 apareceu {tupla.count(9)} {"vezes" if tupla.count(9) != 1 else "vez"}.')
if tupla.count(3) == 0:
    print('O valor 3 não foi digitado em nenhuma posição.')
else:
    print(f'O primeiro valor 3 foi digitado na {tupla.index(3) + 1}ª posição.')
print('Os números pares digitados foram: ', end='')
for n in tupla:
    if n % 2 == 0:
        print(f'{n}', end=' ')