def format_moeda(valor=0, moeda='R$'):
    return f"{moeda}{str(f'{valor:.2f}').replace('.', ',')}"


def aumentar(num=0, percentual=0, formato=False):
    resultado = num * (1 + percentual / 100)
    if formato == True:
        return format_moeda(resultado)
    else:
        return resultado


def diminuir(num=0, percentual=0, formato=False):
    resultado = num * (1 - percentual/100)
    if formato == True:
        return format_moeda(resultado)
    else:
        return resultado


def dobro(num=0, formato=False):
    resultado = num * 2
    if formato == True:
        return format_moeda(resultado)
    else:
        return resultado


def metade(num=0, formato=False):
    resultado = num / 2
    if formato == True:
        return format_moeda(resultado)
    else:
        return resultado


def resumo(valor=0, aumento=0, reducao=0):
    dobrado = dobro(valor, True)
    dividido_metade = metade(valor, True)
    aumentado = aumentar(valor, aumento, True)
    diminuido = diminuir(valor, reducao, True)
    valor = format_moeda(valor)
    print('\033[1:33m-'*35)
    print(f'{"RESUMO DO VALOR":^35}')
    print('-' * 35, end='\033[m\n')
    print(f'{"Preço analisado: ":<20}{valor}')
    print(f'{"Dobro do preço: ":<20}{dobrado}')
    print(f'{"Metade do preço: ":<20}{dividido_metade}')
    print('{:<20}{}'.format(f'{aumento}% de aumento: ', aumentado))
    print('{:<20}{}'.format(f'{reducao}% de reducao: ', diminuido))


