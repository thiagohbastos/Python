print('{}{}{}'.format('\033[1;40m', '-=-'*13, '\033[m'))
print('{}{: ^39}{}'.format('\033[1;32m', 'Gerenciador de Pagamentos', '\033[m'))
print('{}{}{}'.format('\033[1;40m', '-=-'*13, '\033[m'))

p = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no crédito
[ 4 ] 3x ou mais no crédito
''')
op = int(input('Qual a opção desejada? '))

if op == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f} com o desconto de 10%.'.format(p, p * 0.9))
elif op == 2:
    print('Sua compra de R${:.2f} vai custar R${:.2f} com um desconto de 5%.'.format(p, p * 0.95))
elif op == 3:
    print('Sua compra será parcelada em 2x de R${:.2f} sem juros.'.format(p / 2))
elif op == 4:
    pa = int(input('Quantas parcelas? '))
    if pa >= 3:
        cj = p * ( 1.06 ** pa )
        print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(pa, cj / pa))
        print('Sua compra de R${:.2f} vai custar R${:.2f} devido juros de {}6% ao mês{}.'.format(p, cj, '\033[1:31m', '\033[m'))
    else:
        print('Favor voltar ao menu e selecionar uma das opções disponíveis.')
else:
    print('Por favor, selecione uma das opções do menu.')
