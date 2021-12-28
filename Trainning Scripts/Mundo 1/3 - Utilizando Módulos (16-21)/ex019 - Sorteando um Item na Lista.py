from random import choice
print('Prezado professor, gentileza informar o nome dos 4 alunos para sorteio de quem apagará o quadro.')
al1 = str(input('1º Aluno(a): '))
al2 = str(input('2º Aluno(a): '))
al3 = str(input('3º Aluno(a): '))
al4 = str(input('4º Aluno(a): '))
lista = [al1, al2, al3, al4]
escolhido = choice(lista)
print('O aluno(a) escolhido foi o(a) {}!'.format(escolhido))
