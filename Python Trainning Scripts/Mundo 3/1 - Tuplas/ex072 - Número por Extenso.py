extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
           'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    n = int(input('Digite um número inteiro entre 0 e 20: '))
    if n in range (0, 21):
        break
    else:
        print('Tente novamente. ', end='')
print(f'Você digitou o número {extenso[n]}')