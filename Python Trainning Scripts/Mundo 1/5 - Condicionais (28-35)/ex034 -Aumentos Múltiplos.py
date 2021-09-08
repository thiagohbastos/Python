s = float(input('Favor informar o valor do salário a ser recalculado: R$'))
if s > 1250:
    s = s * 1.1
else:
    s = s * 1.15
print('O salário com reajuste será de R${:.2f}'.format(s))