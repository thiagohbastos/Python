def leiaInt(msg):
    while True:
        resp = input(msg)
        if resp.isnumeric():
            resp = int(resp)
            break
        else:
            print('\033[1:31mERRO! Digite um número inteiro válido.\033[m')
    return resp


print('-' * 40)
n = leiaInt('Digite um inteiro: ')
print(f'Você acabou de digitar o número {n}.')
