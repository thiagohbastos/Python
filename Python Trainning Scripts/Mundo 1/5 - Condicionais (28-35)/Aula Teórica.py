tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Seu carro é novo!')
else:
    print('Seu carro é velho.')
#OU
#print('Seu carro é novo!' if tempo <= 3 else 'Seu carro é velho.')

print('{:-^18}'.format('Fim'))