nome = input('Por favor, digite seu nome completo: \n').strip()
fn = nome[:nome.find(' ')]
print('Seu nome em maiúsculas: {}'.format(nome.upper()))
print('Seu nome em minúsculas: {}'.format(nome.lower()))
print('{}, seu nome completo possui {} letras. \nJá seu primeiro nome possui {} letras.'.format(
    fn, len(nome.replace(' ', '')), len(fn)
    ))

