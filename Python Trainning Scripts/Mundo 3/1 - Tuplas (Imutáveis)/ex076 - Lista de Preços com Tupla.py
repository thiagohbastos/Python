lista = ('Cerveja importada', 12.30, 'Cerveja nacional (0,5 litros)', 5.50, 'Garrafa de vinho', 134.90,
         'Água (garrafa de 1,5 litros)', 2.96, 'Alface (1 unidade)', 2.83, 'Cebolas (1kg)', 4.50, 'Batatas (1 kg)', 4.50,
         'Tomates (1 kg)', 6.00, 'Laranjas (1 kg)', 4.60, 'Bananas (1kg)', 5.00, 'Maçãs (1 kg)', 7.10,
         'Queijo fresco (1 kg)', 37.00, 'Uma dúzia de ovos', 8.60, 'Arroz (1 kg)', 6.10, 'Pão (1 kg)', 6.70,
         'Leite (1 litro)', 4.10)

print('\033[1;33m-'*40)
print('{: ^40}'.format('LISTAGEM DE PREÇOS'))
print('-'*40, end='\033[m \n')
for alimento in range (0, len(lista), 2):
    print('{:.<30}R$ {: >5.2f}'.format(lista[alimento], lista[alimento + 1]))
print('\033[1;33m-\033[m'*40)