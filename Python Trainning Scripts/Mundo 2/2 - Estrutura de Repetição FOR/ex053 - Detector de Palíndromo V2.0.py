f = str(input('Digite uma frase: ')).upper().split()
f = ''.join(f)

print('O inverso de {} é {}.'.format(f, f[::-1]))
if f == f[::-1]:
    print('A frase digitada É UM PALÍNDROMO!')
else:
    print('A frase digitada NÃO É um palíndromo!')