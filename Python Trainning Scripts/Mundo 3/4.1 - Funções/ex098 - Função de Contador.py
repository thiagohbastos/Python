from time import sleep
def contagem(inicio, fim, passo):
    print('\033[1:33m-\033[m' * 40)
    if passo == 0:
        passo = 1
    if fim > inicio:
        passo = abs(passo)
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
        for n in range (inicio, fim + 1, passo):
            sleep(0.5)
            print(n, end=' ')
    else:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
        passo = - abs(passo)
        for n in range(inicio, fim - 1, passo):
            sleep(0.5)
            print(n, end=' ')
    print('FIM!')
    sleep(1)


contagem(1, 10, 1)
contagem(10, 1, 2)
print('\033[1:33m-\033[m' * 40)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
contagem(i, f, p)