palavras = ('Assembleia', 'Heroico', 'Ideia', 'Jiboia', 'Arguis', 'Arguem', 'Redarguis', 'Redarguem', 'aluna',
            'apenas', 'conseguiu', 'nota', 'custa', 'muito', 'esforço')
base = ('a', 'e', 'i', 'o', 'u')

for cont in range (0, len(palavras)):
    print(f'Na palavra "{palavras[cont]}" temos as vogais: ', end='')
    for vogal in base:
        if vogal in palavras[cont]:
            print(vogal, end=' ')
    print('')
