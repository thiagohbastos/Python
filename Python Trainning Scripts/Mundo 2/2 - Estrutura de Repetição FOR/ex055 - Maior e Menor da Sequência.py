print('\033[1:36m{:-^40}\033[m'.format('ANALISADOR DE PESOS'))
maior = 0
menor = 0
for c in range (1, 6):
    peso = float(input('Favor informar o {}º peso: (Kg) '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('O maior peso digitado foi {}Kg e o menor foi {}Kg.'.format(maior, menor))
