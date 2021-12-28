print('{}={}'.format('\033[1m', '\033[m') * 40)
print('{}{: ^40}{}'.format('\033[1;33m', 'BANCO BASTOS', '\033[m'))
print('{}={}'.format('\033[1m', '\033[m') * 40)

while True:
    valor = int(input('Que valor você quer sacar? R$'))
    if valor > 0:
        break
tot50 = tot20 = tot10 = tot1 = 0
saldo = valor
while True:
    while saldo // 50 >= 1:
        tot50 += 1
        saldo -= 50
    while saldo // 20 >= 1:
        tot20 += 1
        saldo -= 20
    while saldo // 10 >= 1:
        tot10 += 1
        saldo -= 10
    while saldo // 1 >= 1:
        tot1 += 1
        saldo -= 1
    if saldo <= 0:
        break
if tot50 >= 1:
    print(f'Total de {tot50} cédulas de R$50')
if tot20 >= 1:
    print(f'Total de {tot20} cédulas de R$20')
if tot10 >= 1:
    print(f'Total de {tot10} cédulas de R$10')
if tot1 >= 1:
    print(f'Total de {tot1} cédulas de R$1')
print('{}={}'.format('\033[1m', '\033[m') * 40)
