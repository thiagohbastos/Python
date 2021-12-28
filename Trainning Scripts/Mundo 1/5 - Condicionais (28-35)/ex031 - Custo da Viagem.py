d = float(input('Qual a distância da viagem (Km)? '))
if d <= 200:
    p = 0.5 * d
else:
    p = 0.45 * d
print('O preço da passagem é R${:.2f}'.format(p))