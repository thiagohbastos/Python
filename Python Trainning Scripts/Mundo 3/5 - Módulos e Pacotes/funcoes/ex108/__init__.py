def format_moeda(valor=0, moeda='R$'):
    return f"{moeda}{str(f'{valor:.2f}').replace('.', ',')}"