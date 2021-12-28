from random import shuffle
print('Prezado professor, gentileza informar o nome dos 4 alunos para sorteio de quem apagará o quadro.')
al1 = str(input('1º Aluno(a): '))
al2 = str(input('2º Aluno(a): '))
al3 = str(input('3º Aluno(a): '))
al4 = str(input('4º Aluno(a): '))
ordem = [al1, al2, al3, al4]
shuffle(ordem)
print('A órdem de apresentação será: \n{}'.format(ordem))