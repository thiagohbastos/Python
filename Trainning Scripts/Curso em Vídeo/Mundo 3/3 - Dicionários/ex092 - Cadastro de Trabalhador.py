from datetime import date

cadastro = {}

cadastro['nome'] = str(input('Nome: ')).strip().title()
cadastro['idade'] = date.today().year - int(input('Ano de Nascimento: '))
while True:
    cadastro['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
    if cadastro['CTPS'] >= 0:
        break
    print('\033[1:31mCTPS inválida! \033[m')
nascimento = date.today().year - cadastro['idade']
if cadastro['CTPS'] != 0:
    cadastro['contratação'] = int(input('Ano de Contratação: '))
    cadastro['salário'] = float(input('Salário: R$'))
    cadastro['aposentadoria'] = cadastro['contratação'] + 35 - nascimento
print('-'*40)
for k, v in cadastro.items():
    print(f'- {k.title()} tem o valor {v}')
