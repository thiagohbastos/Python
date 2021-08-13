nome = str(input('Olá Professor! Favor digitar o nome do aluno: '))
nprov = int(input('Agora o número de provas realizadas: '))
nota = 0
cont = 1
s = 0
while cont <= nprov:
    nota = float(input('Favor digitar o valor da {}ª prova: '.format(cont)))
    s = s + nota
    cont = cont + 1
print()
m = s / nprov
print('A média do(a) {} é {:.2f}'.format(nome, m))