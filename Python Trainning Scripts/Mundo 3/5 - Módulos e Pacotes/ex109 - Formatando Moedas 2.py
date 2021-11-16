from funcoes import ex109

p = float(input('Digite o preço: R$'))
print(f'A metade de {ex109.format_moeda(p)} é {ex109.metade(p, True)}')
print(f'O dobro de {ex109.format_moeda(p)} é {ex109.dobro(p, True)}')
print(f'Aumentando 10% de {ex109.format_moeda(p)}, temos {ex109.aumentar(p, 10, True)}')
print(f'Reduzindo 13% de {ex109.format_moeda(p)}, temos {ex109.diminuir(p, 13, True)}')