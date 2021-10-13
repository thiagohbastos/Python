matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_terceira = 0

for l in range (0, 3):
    for c in range (0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l} , {c}]: '))

print('\033[1:35m=-\033[m'*20)
for l in range (0, 3):
    for c in range (0, 3):
        elemento = matriz[l][c]
        print(f'[{matriz[l][c]: ^5}]', end='')
        if elemento % 2 == 0:
            soma_pares += elemento
        if c == 2:
            soma_terceira += elemento
    print()

print('\033[1:35m=-\033[m'*20)

print(f'''A soma dos valores pares é {soma_pares}.
A soma dos valores da terceira coluna é {soma_terceira}.
O maior valor da segunda linha é {max(matriz[1])}.''')