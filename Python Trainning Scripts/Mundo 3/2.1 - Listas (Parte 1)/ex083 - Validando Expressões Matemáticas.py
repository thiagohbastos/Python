expressao = str(input('Digite sua expressão: '))
auxiliar = []

for caractere in expressao:
    if caractere == '(':
        auxiliar.append(caractere)
    elif caractere == ')' and len(auxiliar) > 0:
        auxiliar.pop()
    print(auxiliar)

print('Sua expressão está ', end='')
if expressao.count('(') != expressao.count(')'):
    print('inválida!')
elif len(auxiliar) > 0:
    print('inválida!')
else:
    print('válida!')