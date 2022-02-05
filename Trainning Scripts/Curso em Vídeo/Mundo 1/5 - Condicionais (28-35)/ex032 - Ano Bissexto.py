from datetime import date
a = int(input('Digite um ano para verificação (coloque zero para o ano atual): '))
if a == 0:
    a = date.today().year
if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0):
    print('O ano {} é Bissexto!'.format(a))
else:
    print('O ano {} não é Bissexto!'.format(a))