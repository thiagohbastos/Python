altura = float(input('Favor informar a altura da parede que será pintada: '))
comp = float(input('Agora seu comprimento: '))
print('Tendo em vista que 1L de tinta pinta 2m² de área, serão necessários {:.2f}L de tinta para pintar essa parede.'.format((altura * comp)/2))