lanche = ['Sanduiche', 'Suco', 'Pizza', 'Pudim']
print(lanche)

#Trocando valores da lista
lanche[3] = 'Picolé'
print(lanche)

#Adicionando valores à lista
lanche.append('Cookie')
print(lanche)

#Adicionando valores em posições específicas
lanche.insert(1, 'Cachorro-quente')
print(lanche)

#Maiores e menores valores
print(max(lanche))
print(min(lanche))

#Deletando um item da lista
del lanche[3] # ou lanche.pop(3) ou lanche.remove('Suco'), no caso do remove só é deletada a primeira ocorrência
print(lanche)

#Criando listas com range
valores = list(range(4, 11, 2))
print(valores)

#Organizando valores
lanche.sort()
valores.sort(reverse=True)
print(lanche, '\n', valores)

#Tamanho da lista (número de elementos)
len(lanche)

#Realizando ligações entre listas:
lanche1 = lanche
#Realizando cópia de uma lista
lanche1 = lanche[:]