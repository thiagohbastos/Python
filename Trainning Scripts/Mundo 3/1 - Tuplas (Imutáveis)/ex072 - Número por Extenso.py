extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
           'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    while True:
        n = int(input('Digite um número inteiro entre 0 e 20: '))
        if n in range (0, 21):
            break
        print('Tente novamente. ', end='')
    print(f'Você digitou o número {extenso[n]}.')
    while True:
        resp = str(input('Gostaria de continuar? [S/N] ')).strip().upper()
        if resp in 'NS':
            break
    if resp == 'N':
        break