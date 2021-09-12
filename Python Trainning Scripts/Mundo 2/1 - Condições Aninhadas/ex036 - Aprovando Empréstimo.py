print('{}{}{}'.format('\033[1;30;47m', '-=-'*13, '\033[m'))
print('{}{: ^39}{}'.format('\033[1;34m', 'Aprovando um Empréstimo', '\033[m'))
print('{}{}{}'.format('\033[1;30;47m', '-=-'*13, '\033[m'))

from time import sleep

v = float(input('Favor informar o valor da casa: R$'))
s = float(input('Agora informe o salário do comprador: R$'))
t = float(input('O empréstimo pretende ser pago em quantos anos? '))
r = v/(t*12)
print('-' * 39)
print('Calculando...')
sleep(1)
print('O valor da mensalidade para os parâmetros acima seria de: R${:.2f}'.format(r))
sleep(2)
if r > 0.3 * s:
    print('-' * 39)
    print('{}{: ^39}{}'.format('\033[1:31m', 'EMPRÉSTIMO NEGADO', '\033[m'))
    print('-' * 39)
    print('{: ^39}'.format('O Valor da mensalidade excede 30% do salário do comprador!'))
else:
    print('-' * 39)
    print('{}{: ^39}{}'.format('\033[1:32m', 'EMPRÉSTIMO LIBERADO', '\033[m'))
    print('-' * 39)