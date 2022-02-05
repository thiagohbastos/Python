aluno = dict()
aluno['nome'] = str(input('Nome do aluno: ')).strip().title()
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
print('{}-{}'.format('\033[1:34m', '\033[m')*40)

if aluno['média'] >= 7:
    aluno['situação'] = '{}APROVADO{}'.format('\033[1:32m', '\033[m')
elif 7 > aluno['média'] >= 5:
    aluno['situação'] = '{}EM RECUPERAÇÃO{}'.format('\033[1:33m', '\033[m')
else:
    aluno['situação'] = '{}REPROVADO{}'.format('\033[1:31m', '\033[m')

for k, v in aluno.items():
    print(f'{k} é igual a {v}.')
