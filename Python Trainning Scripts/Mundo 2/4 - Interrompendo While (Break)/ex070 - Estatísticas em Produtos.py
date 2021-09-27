print('{}-{}'.format('\033[1m', '\033[m') * 30)
print('{}{: ^30}{}'.format('\033[1;32m', 'LOJA SUPER BARATÃO', '\033[m'))
print('{}-{}'.format('\033[1m', '\033[m') * 30)

total = acimamil = maisbarato = 0

while True:
    preço = 0
    resp = 'reset'
    nome = str(input('Nome do Produto: ')).strip().capitalize()
    while preço <= 0:
        preço = float(input('Preço: R$'))
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    total += preço
    if preço > 1000:
        acimamil += 1
    if maisbarato == 0 or preço < maisbarato:
        maisbarato = preço
        prodmaisbarato = nome
    if resp == 'N':
        break
    print('{}-{}'.format('\033[1m', '\033[m') * 30)
print(f'''{' FIM DO PROGRAMA ':-^30}
O total da compra foi R${total:.2f}
Temos {acimamil} {'produto' if acimamil == 1 else 'produtos'} custando mais de R$1000.00
O produto mais barato e seu preço: {prodmaisbarato}, custando R${maisbarato:.2f}''')
