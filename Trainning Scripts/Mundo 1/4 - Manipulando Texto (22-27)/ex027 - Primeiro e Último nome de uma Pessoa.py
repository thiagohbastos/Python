nome = input('Favor digitar um nome completo: \n').strip().title().split()
cont = len(nome)
fn = nome[0]
ln = nome[cont-1]
print('Muito prazer em te conhecer!\nSeu primeiro nome é {}\nSeu último nome é {}'.format(fn, ln))
