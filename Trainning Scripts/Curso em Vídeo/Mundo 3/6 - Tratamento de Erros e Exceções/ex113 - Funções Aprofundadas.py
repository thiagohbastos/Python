def leiaInt(mensagem):
    while True:
        try:
            inteiro = int(input(mensagem).strip())
        except Exception as tipo_erro:
            print(f'\033[1:31mERRO {tipo_erro.__class__}! Por favor, digite um número inteiro válido.\033[m')
        else:
            return inteiro
        finally:
            print('\033[1:33m-' * 60, end='\033[m\n')


def leiaReal(mensagem):
    while True:
        try:
            real = float(input(mensagem))
        except Exception as tipo_erro:
            print(f'\033[1:31mERRO {tipo_erro.__class__}! Por favor, digite um número inteiro válido.\033[m')
        else:
            return real
        finally:
            print('\033[1:33m-' * 60, end='\033[m\n')


inteiro_v = leiaInt('Digite um Inteiro: ')
real_v = leiaReal('Digite um Real: ')
print(f'O valor inteiro foi {inteiro_v} e o real foi {real_v}')