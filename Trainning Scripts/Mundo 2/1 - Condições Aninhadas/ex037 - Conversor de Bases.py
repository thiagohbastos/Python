print('{}{}{}'.format('\033[1;40m', '-=-'*13, '\033[m'))
print('{}{: ^39}{}'.format('\033[1;35m', 'Conversor de Bases', '\033[m'))
print('{}{}{}'.format('\033[1;40m', '-=-'*13, '\033[m'))

n = int(input('Favor informar um número para conversão de base: '))
b = int(input('''Agora, selecione uma das bases abaixo para conversão.
1 - Para Binário
2 - Para Octal
3 - Para Hexadecimal
Sua escolha: '''))
if b == 1:
    print('{} convertido em Binário é igual a {}'.format(n, bin(n)[2:]))
elif b == 2:
    print('{} convertido em Octal é igual a {}'.format(n, oct(n)[2:]))
elif b == 3:
    print('{} convertido em Hexadecimal é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Apenas as opções de 1 a 3 estão disponíveis.')