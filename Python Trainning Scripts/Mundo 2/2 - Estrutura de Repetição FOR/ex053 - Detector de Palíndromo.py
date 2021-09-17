f = str(input('Digite uma frase: ')).strip().upper().split()
f = ''.join(f)
print('O inverso de {} é'.format(f), end=' ')
for c in range (len(f), 0, -1):
    print(f[c - 1], end='')

i = 'É'
for c in range (len(f), 0, -1):
    if f[c - 1] != f[len(f) - c]:
        i = 'NÃO É'

print('\nA frase {} um palíndromo!'.format(i))



