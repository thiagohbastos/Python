totidade = 0
idadehmaisv = 0
nomehmaisv = ''
contf = 0

for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()

    totidade += idade
    if idade > idadehmaisv and sexo == 'M':
        idadehmaisv = idade
        nomehmaisv = nome

    if sexo == 'F' and idade < 20:
        contf += 1
mediaidade = totidade / p

print('A idade média do grupo é {} anos.'.format(mediaidade))
if nomehmaisv == '':
    print('Não foram informados os dados de nenhum homem, por isso não há um homem mais velho!')
else:
    print('O nome do homem mais velho é {} e ele tem {} anos.'.format(nomehmaisv.upper(), idadehmaisv))
if contf == 0:
    print('Não foram informadas mulheres com menos de 20 anos.')
else:
    print('Foram informados os dados de {} mulher(s) com menos de 20 anos.'.format(contf))

