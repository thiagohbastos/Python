def linha(tam=42):
    return '-' * tam


def cabeçalho(texto):
    print(linha())
    print(texto.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[1:33m{c}\033[m - \033[1:34m{item}\033[m')
        c += 1
    print(linha())
    resp = leiaInt('\033[1:32mSua Opção:\033[m ')
    return resp


def leiaInt(mensagem):
    while True:
        try:
            inteiro = int(input(mensagem).strip())
        except Exception as tipo_erro:
            print(f'\033[1:31mERRO {tipo_erro.__class__}! Por favor, digite um número inteiro válido.\033[m')
        else:
            return inteiro
        finally:
            print('-' * 42)


