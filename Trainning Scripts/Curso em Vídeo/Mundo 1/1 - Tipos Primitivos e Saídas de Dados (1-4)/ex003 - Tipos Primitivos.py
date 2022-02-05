#tipos primitivos: str, int, float and bool(True and False).
nome = str(input('Olá! Qual o seu nome? '))
n1 = float(input('{} , por favor, digite um número: '.format(nome)))
n2 = float(input('Digite mais um número '))
s = float(n1 + n2)
print('Então', nome, ', a soma entre {} e {} é {}'.format(n1, n2, s))
#print(type(s))

