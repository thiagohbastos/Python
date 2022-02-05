print('Vamos analisar três números inteiros de sua preferência!')
n1 = int(input('1º número: '))
n2 = int(input('2º número: '))
n3 = int(input('3º número: '))
lista = [n1, n2, n3]
lista.sort()
print('O menor número digitado foi {}, enquanto o maior foi {}.'.format(lista[0], lista[2]))
