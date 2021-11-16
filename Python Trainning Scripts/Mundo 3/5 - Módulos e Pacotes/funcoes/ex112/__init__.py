def leiaDinheiro(msg):
    while True:
        valor = input(msg).replace(',', '.').strip()
        if valor.isalpha() or valor == '':
            print(f'\033[1:31mERRO: "{valor}" é um preço inválido!\033[m')
        else:
            valor = float(valor)
            return valor
            break
