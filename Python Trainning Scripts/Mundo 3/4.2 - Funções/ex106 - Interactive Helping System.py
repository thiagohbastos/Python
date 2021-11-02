def ajuda(função):
    mensagem = f'Acessando o manual do comando {função.upper()}'
    tamanho = len(mensagem) + 10

    print(f'\033[1:30:44m-' * tamanho)
    print(f'{mensagem:^{tamanho}}')
    print(f'-' * tamanho)

    print('\033[7m')
    return help(função)


while True:
    print('\033[1:30:43m-' * 40)
    print(f'{"SISTEMA DE AJUDA PyHELP":^40}')
    print('-' * 40)

    comando = str(input('\033[mFunção ou Biblioteca > ')).strip()
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
        print('\033[m')
print('\033[1:30:41m-' * 30)
print(f'{"ATÉ LOGO":^30}')
print('-' * 30)