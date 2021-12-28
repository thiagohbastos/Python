from math import hypot
print('Vamos calcular a hipotenusa de um triângulo retângulo \n', '-'*51)
c1 = abs(float(input('Favor informar o tamanho do primeiro cateto: ')))
c2 = abs(float(input('Agore informe o tamanho do segundo cateto: ')))
h = hypot(c1 ,c2)
print('A hipotenusa de um triângulo retângulo com catetos {} e {} medirá {:.2f}'.format(c1, c2, h))
