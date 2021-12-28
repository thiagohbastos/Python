v = float(input('Qual a velocidade observada (Km/h)? '))
if v > 80:
    print('Favor efetuar uma MULTA DE EXCESSO DE VELOCIDADE para o veículo em questão.')
    print('VALOR DA MULTA: R${:.2f}'.format((v - 80)*7))
else:
    print('Veículo em velocidade regular.')
print('{:-^30}'.format('ENCERRANDO'))
