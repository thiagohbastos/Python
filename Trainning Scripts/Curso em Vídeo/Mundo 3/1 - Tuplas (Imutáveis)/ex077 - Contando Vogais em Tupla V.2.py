palavras = ('Assembleia', 'Heroico', 'Ideia', 'Jiboia', 'Arguis', 'Arguem', 'Redarguis', 'Redarguem', 'aluna',
            'apenas', 'conseguiu', 'nota', 'custa', 'muito', 'esforço')

for cont in range (0, len(palavras)):
    print(f'Na palavra "{palavras[cont]}" temos as vogais: ', end='')
    for letra in range (0, len(palavras[cont])):
        if palavras[cont][letra] in 'aeiou':
            print(palavras[cont][letra], end=' ')
    print('')
