print('{}{}{}'.format('\033[1;40m', '-=-'*13, '\033[m'))
print('{}{: ^39}{}'.format('\033[1;33m', 'Alistamento Militar', '\033[m'))
print('{}{}{}'.format('\033[1;40m', '-=-'*13, '\033[m'))

from datetime import date
anoatual = date.today().year
from math import fabs

idade = int(input('Favor informar o ano de nascimento: '))
dif = anoatual - idade -18
if dif == 0 :
    print('{}Caso ainda não tenha se alistado, você deverá se alistar ainda este ano!'.format('\033[1:33m'))
elif dif < 0 and dif >= -1:
    print('{}Você deverá se alistar no ano que vem!'.format('\033[1:32m'))
elif dif < -1:
    print('{}Você deverá se alistar em {:.0f} anos!'.format('\033[1:32m', fabs(dif)))
else:
    print('{}Você deveria ter se alistado em {}! Procure uma junta militar para regularizar sua situação.'.format('\033[1:31m', idade + 18))