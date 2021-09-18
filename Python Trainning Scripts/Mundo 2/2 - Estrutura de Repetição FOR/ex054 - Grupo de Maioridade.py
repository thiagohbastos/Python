from datetime import date
hoje = date.today()
print('''{:-^50}
O formato padrão será como o exemplo: {}27/06/1991{}
{:-^50}'''.format(' CADASTRO DATA DE NASCIMENTO ', '\033[1:33m', '\033[m', ''))
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    n = input('Favor digitar a {}ª data de nascimento: '.format(pess)).strip().replace('/', ' ').split()
    n = [int(n[2]), int(n[1]), int(n[0])]
    n = date(n[0], n[1], n[2])
    i = (hoje - n).days/365.25
    if i >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade.\nTambém tivemos {} pessoas menores de idade.'.format(totmaior, totmenor))

