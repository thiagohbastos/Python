frase = input('Favor digitar uma frase ou texto: ').lower().strip()
x = frase.count('a')
p = frase.find('a') + 1
u = frase.rfind('a') + 1 - frase.count(' ')
print('A frase digitada possui {} ocorrências da letra "A". \nSua primeira ocorrência foi na {}ª posição. \n'
      'Já sua última ocorrência foi na {}ª posição'.format(x, p, u))