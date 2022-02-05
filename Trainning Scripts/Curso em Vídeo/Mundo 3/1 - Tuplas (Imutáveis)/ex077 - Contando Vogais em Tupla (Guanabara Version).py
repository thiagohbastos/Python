palavras = ('Assembleia', 'Heroico', 'Ideia', 'Jiboia', 'Arguis', 'Arguem', 'Redarguis', 'Redarguem', 'aluna',
            'apenas', 'conseguiu', 'nota', 'custa', 'muito', 'esforço')

for p in palavras:
    print(f'Na palavra "{p.upper()}" temos as vogais: ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')
    print('')
