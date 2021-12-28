print('\033[0;30;41mTeste\033[m')
print('\033[1:36:40mTeste\033[m')
print('\033[7:33mTeste\033[m')
print('\033[1:35mTeste')
print('\033[4:31mTeste')
print('\033[4:30:45mTeste\033[m')

print('{}Teste{}'.format('\033[7m','\033[m'))

cores = {'limpa':'\033[m',
         'azul':'\033[1:34m',
         'amarelo':'\033[1:33m'}

print('{}Teste{}'.format(cores ['amarelo'], cores['limpa']))