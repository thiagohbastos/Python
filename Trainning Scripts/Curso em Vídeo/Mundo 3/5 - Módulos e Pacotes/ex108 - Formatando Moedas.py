from funcoes import ex107, ex108

p = float(input('Digite o preço: R$'))
print(f'A metade de {ex108.format_moeda(p)} é {ex108.format_moeda(ex107.metade(p))}')
print(f'O dobro de {ex108.format_moeda(p)} é {ex108.format_moeda(ex107.dobro(p))}')
print(f'Aumentando 10% de {ex108.format_moeda(p)}, temos {ex108.format_moeda(ex107.aumentar(p, 10))}')
print(f'Reduzindo 13% de {ex108.format_moeda(p)}, temos {ex108.format_moeda(ex107.diminuir(p, 13))}')