from datetime import date


def voto(idade):
    """
    :param nascimento: Data de Nascimento para avaliação de voto.
    :return: status de voto, sendo NEGADO, OPCIONAL ou OBRIGATÓRIO
    """

    if 16 <= idade < 18 or idade > 65:
        return 'VOTO OPCIONAL'
    elif idade >= 18:
        return 'VOTO OBRIGATÓRIO'
    else:
        return 'NÃO VOTA'


print('-' * 40)
nasc = int(input('Em que ano você nasceu? '))
idade = date.today().year - nasc
print(f'Com {idade} anos: {voto(idade)}')
