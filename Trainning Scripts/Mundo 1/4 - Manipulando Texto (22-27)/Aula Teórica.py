frase = 'Curso em Vídeo Python'
print(frase[9]) #string na 9ª posição
print(frase[9:21]) #string da 9ª à 21ª posição
print(frase[9:21:2]) #string da 9ª à 21ª posição contando de 2 em 2 caracteres
print(frase[:5]) # é = frase[0:5]
print(frase[15:]) # é = frase da 15ª até o final
print(frase[9::3]) #mesma lógica das anteriores
print(frase[::-1]) #frase ao contrário

#Análise
print(len(frase)) # número de strings
print(frase.count('o')) # número de ocorrências da string
print(frase.count('o', 0, 13)) # número de ocorrências da string com fatiamento
print(frase.find('deo')) # posição da string caso exista, senão -1
print('Curso' in frase) # resultado boleano sobre a existência da string

#Transformação
print(frase.replace('Python', 'Android'))
print(frase.upper()) # ou print(frase.lower())
print(frase.capitalize()) # apenas a primeira letra em maiúscula
print(frase.title()) # todas as primeiras letras em maiúsculo

frase = '   Aprenda Python  '
print(frase.strip()) #remove os espaços no início e fim da string
print(frase.rstrip()) #como anterior na parte direita. Já lstrip parte esquerda

#Divisão
frase = 'Curso em Vídeo Python'
frase = frase.split() #divide as palavras em uma lista
#Junção
print('-'.join(frase))

