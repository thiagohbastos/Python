def notas(* valor, sit = False):
    """
    Retorna o total de notas cadastradas, a maior e menor nota, a média e a situação (opcional) do aluno.
    :param valor: (multiplas) notas cadastradas
    :param sit: (opcional) boolean para ver ou não a situação do aluno - padrão 'False'
    :return: dict (um dicionário)
    """
    base = dict()
    base['total'] = len(valor)
    base['maior'] = max(valor)
    base['menor'] = min(valor)
    base['média'] = float(f'{(sum(valor) / len(valor)):.2f}')
    if sit:
        if base['média'] < 5:
            base['situação'] = 'RUIM'
        elif 7 > base['média'] >= 5:
            base['situação'] = 'RAZOÁVEL'
        else:
            base['situação'] = 'BOA'
    return base


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)
