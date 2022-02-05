sexo = str(input('Favor digitar o sexo de uma pessoa [M/F]: ')).upper().strip()
while sexo not in 'MF':
    sexo = str(input('{}Opção inválida!{}\nFavor informar um sexo: '.format('\033[1:31m', '\033[m'))).upper().strip()
print('Sexo {}{}{} registrado com sucesso.'.format('\033[2:33m', sexo, '\033[m'))
