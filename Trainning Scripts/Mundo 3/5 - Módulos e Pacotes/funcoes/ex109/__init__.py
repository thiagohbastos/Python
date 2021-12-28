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


