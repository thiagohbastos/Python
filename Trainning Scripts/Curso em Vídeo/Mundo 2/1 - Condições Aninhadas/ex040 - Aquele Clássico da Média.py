print('{}{}{}'.format('\033[1;40m', '-=-'*13, '\033[m'))
print('{}{: ^39}{}'.format('\033[1;32m', 'Aquele Clássico da Média', '\033[m'))
print('{}{}{}'.format('\033[1;40m', '-=-'*13, '\033[m'))

p1 = float(input('Primeira nota: '))
p2 = float(input('Segunda nota: '))
m = (p1 + p2)/2
print('Tirando {} e {}, a média do aluno é {:.1f}'.format(p1, p2, m))
if m >= 7:
    print('O aluno está {}APROVADO{}!'.format('\033[1:32m', '\033[m'))
elif m < 7 and m >= 5:
    print('O Aluno está em {}RECUPERAÇÃO{}!'.format('\033[1:33m', '\033[m'))
else:
    print('O aluno está {}REPROVADO{}!'.format('\033[1:31m', '\033[m'))