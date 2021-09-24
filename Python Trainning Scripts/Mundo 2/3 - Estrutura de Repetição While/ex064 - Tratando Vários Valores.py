n = int(input('Digite um número [{}999 para parar{}]: '.format('\033[1:33m', '\033[m')))
cont = s = 0

while n != 999:
    cont += 1
    s += n
    n = int(input('Digite um número [{}999 para parar{}]: '.format('\033[1:33m', '\033[m')))

if cont == 0:
    print('Você digitou 999 de início. Nenhum valor foi considerado.')
elif cont == 1:
    print('Você digitou apenas o número {}.'.format(s))
else:
    print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, s))
