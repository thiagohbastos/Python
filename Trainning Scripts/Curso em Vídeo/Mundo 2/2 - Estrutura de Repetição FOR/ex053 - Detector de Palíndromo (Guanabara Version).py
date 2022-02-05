f = str(input('Digite uma frase: ')).strip().upper().split()
f = ''.join(f)

inverso = ''
for letra in range(len(f), 0, -1):
    inverso += f[letra - 1]
print('O inverso de {} é {}.'.format(f, inverso))

if f == inverso:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')