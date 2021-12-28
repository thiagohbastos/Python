valores = list()
while True:
    v = int(input('Digite um valor: '))
    if v not in valores:
        valores.append(v)
        print('{}Valor adicionado com sucesso.{}'.format('\033[1:32m', '\033[m'))
    else:
        print('{}Valor duplicado não adicionado.{}'.format('\033[1:31m', '\033[m'))
    while True:
        resp = str(input('Gostaria de continuar? [S/N] ')).strip().upper()
        if resp in 'SN':
            break
    if resp == 'N':
        break
    print('\033[1m--\033[m' * 20)
print('{}{:-^40}{}'.format('\033[1:34m', ' CADASTRO FINALIZADO ', '\033[m'))
print(f'Você digitou os valores {sorted(valores)}')