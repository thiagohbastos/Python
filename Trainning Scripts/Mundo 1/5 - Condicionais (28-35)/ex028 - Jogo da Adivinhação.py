from random import randint
from time import sleep
n = randint(1, 5) # Faz a escolha do computador
print('-=-'*18)
print('Vou pensar em um número de 1 a 5. Tente adivinhar...')
print('-=-'*18)
r = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if r == n:
    print('Você conseguiu me vencer! Eu realmente pensei no número {}.'.format(n))
else:
    print('GANHEI! Eu pensei no número {}, não no {}!'.format(n, r))