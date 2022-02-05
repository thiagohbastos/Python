individuo = dict()
geral, mulheres, acima_media = [], [], []
totidade = 0

while True:
    individuo['nome'] = str(input('Nome: ')).strip().title()
    while True:
        individuo['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
        if individuo['sexo'] in 'MF':
            break
        print('\033[1:31mApenas [M/F]! Tente novamente.\033[m')
    while True:
        individuo['idade'] = int(input('Idade: '))
        if individuo['idade'] >= 0:
            break
        print('\033[1:31mIdade inválida! Tente novamente.\033[m')
    geral.append(individuo.copy())
    totidade += geral[-1]['idade']
    if individuo['sexo'] == 'F':
        mulheres.append(individuo['nome'])
    individuo.clear()
    resp = str(input('Gostaria de continuar? [S/N] ')).strip().upper()
    print('\033[1:33m-\033[m'*50)
    if resp == 'N':
        break

media = totidade / len(geral)
for cont in range(0, len(geral)):
    if geral[cont]['idade'] > media:
        acima_media.append([geral[cont]['nome'], geral[cont]['sexo'], geral[cont]['idade']])
print(f'A) Foram cadastradas {len(geral)} pessoas.')
print(f'B) A média de idade é {media:.2f} anos.')
print(f'C) Lista das mulheres cadastradas: {mulheres}')
print(f'D) Lista das pessoas com idade acima da média ({media}): ')
for cont in range(0, len(acima_media)):
    print(f'    Nome = {acima_media[cont][0]}; sexo = {acima_media[cont][1]}; '
          f'idade = {acima_media[cont][2]}')
