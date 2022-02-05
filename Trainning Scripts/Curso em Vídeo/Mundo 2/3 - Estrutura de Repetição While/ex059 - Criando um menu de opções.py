from time import sleep

n1 = float(input('Favor digitar o primeiro valor: '))
n2 = float(input('Favor digitar o segundo valor: '))

print('----- {}MENU{} -----'.format('\033[1:33m', '\033[m'))
sleep(1)
print('''[1] Soma dos valores
[2] Multiplicação entre os valores
[3] Maior valor
[4] Digitar novos números
[5] Sair do programa
----------------''')

r = int(input('Favor selecionar uma opção: '))

while r != 5:
    if r in range (1, 5, 1):
        if r == 1:
            print('A soma entre {} e {} equivale a {:.1f}!'.format(n1, n2, n1 + n2))
            sleep(3)
        elif r == 2:
            print('O produto entre os números {} e {} equivale a {:.1f}!'.format(n1, n2, n1 * n2))
            sleep(4)
        elif r == 3:
            if n1 > n2:
                m = n1
                print('O maior valor entre os dois números é {}!'.format(m))
            elif n1 < n2:
                m = n2
                print('O maior valor entre os dois números é {}!'.format(m))
            else:
                print('Não há valor maior! Os números informados são iguais!')
        else:
            print('Favor digitar os novos números.')
            n1 = float(input('Primeiro valor: '))
            n2 = float(input('Segundo valor: '))
    else:
        print('{}Favor digitar uma opção válida!{}'.format('\033[1:31m', '\033[m'))
    sleep(1)
    print('----- {}MENU{} -----'.format('\033[1:33m', '\033[m'))
    sleep(1)
    print('''[1] Soma dos valores
[2] Multiplicação entre os valores
[3] Maior valor
[4] Digitar novos números
[5] Sair do programa
----------------''')
    r = int(input('Opção: '))
print('{}--- Programa finalizado ---{}'.format('\033[1:33m', '\033[m'))