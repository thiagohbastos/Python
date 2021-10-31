from time import sleep
def maior (valores):
    print('\033[1:34m=\033[m' * 60)
    print('Analisando os valores passados...\n(', end='')
    maior_v = 0
    if len(valores) != 0:
        for i, v in enumerate(valores):
            if i == 0:
                maior_v = v
            elif v > maior_v:
                maior_v = v
            if i == (len(valores) - 1):
                sleep(0.5)
                print(v, end=')')
                sleep(0.5)
            else:
                sleep(0.5)
                print(v, end=' ')
    else:
        sleep(0.5)
        print('Não foram inforamdos valores)', end='')
        sleep(0.5)
    print(f'\nComo soliitado, foram informados {len(valores)} valores ao todo.')
    print(f'O maior valor informado foi \033[1:35m{maior_v}\033[m!')
    print('\033[1:34m=\033[m' * 60)


valores = list()
while True:
    valores.clear()
    tamanho = int(input('Quantos números gostaria de analisar? '))
    if tamanho != 0:
        for cont in range (1, tamanho + 1):
            valores.append(int(input(f'{cont}º valor: ')))
    maior(valores)
    while True:
        resp = str(input('Gostaria de continuar? [S/N] ')).strip().upper()
        if resp in 'SN':
            break
    if resp == 'N':
        break
print('-- FINALIZANDO --')