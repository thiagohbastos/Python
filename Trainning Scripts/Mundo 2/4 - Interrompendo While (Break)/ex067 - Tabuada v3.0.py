while True:
    n = int(input('Deseja ver a tabuada de qual número? '))
    print('{}-{}'.format('\033[1:36m', '\033[m') * 40)
    if n < 0:
        break
    for multiplicador in range (1, 11, 1):
        print(f'{n} x {multiplicador: <2} = {n * multiplicador}')
    print('{}-{}'.format('\033[1:36m', '\033[m') * 40)
print('PROGRAMA TABUADA ENCERRADO. VOLTE SEMPRE')
