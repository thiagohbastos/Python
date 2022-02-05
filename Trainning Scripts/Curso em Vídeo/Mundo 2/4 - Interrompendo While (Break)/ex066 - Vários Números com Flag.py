s = cont = 0
while True:
    n = int(input('Digite um número [{}999 para parar{}]: '.format('\033[1:33m', '\033[m')))
    if n == 999:
        break
    s += n
    cont += 1
if cont == 0:
    print('Nenhum valor (diferente de 999) foi digitado.')
elif cont == 1:
    print(f'Apenas o valor {s} foi digitado')
else:
    print(f'Foram digitados {cont} valores e a soma entre eles equivale a {s}.')