maisdezoito = homens = mulheresmenos20 = 0

while True:
    print('{}-{}'.format('\033[1m', '\033[m') * 40)
    print('{}{: ^40}{}'.format('\033[1:34m', 'CADASTRE UMA PESSOA', '\033[m'))
    print('{}-{}'.format('\033[1m', '\033[m') * 40)
    idade = 0
    sexo = resp = 'reset'
    while idade <=0:
        idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if idade >= 18:
        maisdezoito += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade <20:
        mulheresmenos20 += 1
    if resp == 'N':
        break
print(f'''{' FIM DO PROGRAMA ':=^40}
Total de pessoas com mais de 18 anos: {maisdezoito}
Ao todo temos {homens} {'homem cadastrado' if homens == 1 else 'homens cadastrados'}.
E temos {mulheresmenos20} {'mulher' if mulheresmenos20 == 1 else 'mulheres'} com menos de 20 anos. ''')