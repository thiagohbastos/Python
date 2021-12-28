def formata(msg):
    tamanho = len(msg) + 15
    print('\033[1:33m-\033[m' * tamanho)
    print(f'{msg:^{tamanho}}')
    print('\033[1:33m-\033[m' * tamanho)

while True:
    mensagem = str(input('Escreva uma mensagem para formatação: ')).strip().capitalize()
    formata(mensagem)
    while True:
        resp = str(input('Gostaria de continuar? [S/N] ')).strip().upper()
        if resp in 'SN':
            break
    if resp == 'N':
        break
    print()
print('-- Finalizando --')
