from funcoes import ex107

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {ex107.metade(p)}')
print(f'O dobro de {p} é {ex107.dobro(p)}')
print(f'Aumentando 10% de {p}, temos {ex107.aumentar(p, 10)}')
print(f'Reduzindo 13% de {p}, temos {ex107.diminuir(p, 13)}')