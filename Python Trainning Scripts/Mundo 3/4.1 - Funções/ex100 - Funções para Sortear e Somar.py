from random import randint
from time import sleep
def sorteio(tamanho, inicio_sorteio, fim_sorteio):
    print('\033[1:34m=\033[m' * 60)
    soma_pares = 0
    valores = list()
    print(f'Sorteando os {tamanho} valores da lista de {inicio_sorteio} à {fim_sorteio}: ', end='')
    for cont in range (0, abs(tamanho)):
        valores.append(randint(inicio_sorteio, fim_sorteio))
        if valores[cont] % 2 == 0:
            soma_pares += valores[cont]
        print(valores[cont], end=' ')
        sleep(0.5)
    print(f'\nSomando os valores pares de {valores}, temos {soma_pares}.')


t = abs(int(input('Quantos valores gostaria de sortear? ')))
i = int(input('Qual o número de início do intervalo de sorteio? '))
f = int(input('E o fim? '))
sorteio(t, i, f)