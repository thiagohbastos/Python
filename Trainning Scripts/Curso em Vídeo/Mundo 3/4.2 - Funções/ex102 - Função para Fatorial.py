def fatorial(valor, show=False):
    """
    Calcula o fatorial de um número
    :param valor: número para saber seu fatorial
    :param show: boolean para demonstrar (True) ou não (False) os calculos realizados
    :return: resultado com ou sem os cálculos.
    """
    resultado = 1
    for cont in range (valor, 0, -1):
        resultado *= cont
    if show == False:
        return resultado
    else:
        for cont2 in range (valor, 0, -1):
            print(cont2, end=f'{" x " if cont2 != 1 else " = "}')
        return resultado


numero = int(input('Valor para fatorial: '))
resp = True if str(input('Gostaria de ver os calculos? [S/N] ').strip().upper()) == 'S' else False
print(fatorial(numero, resp))
