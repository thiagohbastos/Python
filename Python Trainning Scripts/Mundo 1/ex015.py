dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
v = 0.15 * km + dias * 60
print('O total a pagar é de R${:.2f}'.format(v))
