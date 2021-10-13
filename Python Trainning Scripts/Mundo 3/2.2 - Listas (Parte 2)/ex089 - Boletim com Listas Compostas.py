from time import sleep

boletim, alunos, notas = [], [], []

while True:
    alunos.append(str(input('Nome: ')).strip().title())
    for cont1 in range (1,3):
        while True:
            nota = float(input(f'Nota {cont1}: '))
            if nota >= 0 and nota <=10:
                break
            else:
                print('{}Apenas notas entre 0 e 10!{}'.format('\033[1:31m', '\033[m'))
        notas.append(nota)
    alunos.append(notas[:])
    boletim.append(alunos[:])
    alunos.clear(), notas.clear()
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
        if resp in 'SN':
            break
    print('-' * 30)
    if resp == 'N':
        break
print('{: ^3}|{: ^19}|{: ^6}'.format('Nº', ' NOME', ' MÉDIA'))
for cont1 in range (1, len(boletim) + 1):
    print('{: <3}|{: ^19}|{: ^6.2f}'.format(cont1, boletim[cont1-1][0], sum(boletim[cont1-1][1]) / 2))

while True:
    print('-' * 30)
    while True:
        resp2 = int(input('Mostrar as notas de qual aluno? (digite 0 para finalizar) '))
        if resp2 not in range (0, len(boletim) + 1):
            print('{}Aluno não encontrado! Tente novamente.{}'.format('\033[1:31m', '\033[m'))
        else:
            break
    if resp2 == 0:
        break
    sleep(1)
    print(f'Notas de {boletim[resp2 - 1][0]}: {boletim[resp2 - 1][1]}')
print('{:-^30}'.format(' FINALIZANDO '))
sleep(1)
print('\033[1:32m{: ^30}\033[m'.format(' VOLTE SEMPRE! '))
