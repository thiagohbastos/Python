from random import randrange

print('{}-=-{}'.format('\033[1:34m', '\033[m')*18)
print('Vou pensar em um número de 1 a 10. Tente adivinhar...')
print('{}-=-{}'.format('\033[1:34m', '\033[m')*18)

comp = randrange(1, 11, 1)
cont = 1
n = int(input('Qual o seu palpite? '))
while n != comp:
    cont += 1
    if n in range(1, 11):
        print('Você errou! Tente outra vez! ')
    else:
        print('{}Digite um valor dentro do intervalo de 1 a 10! Perdeu uma vida! {}'.format('\033[1:31m', '\033[m'))
    n = int(input('Próxima tentativa: '))
if cont == 1:
    print('Caraca! Você acertou de primeira! Eu realmente escolhi {}.'.format(n))
else:
    print('É... Você acertou! Mas precisou de {} tentativas né? hahaha'.format(cont))