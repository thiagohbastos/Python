# Título da calculadora
print('{:*^61}'.format(' Python Calculator '))

# Menu
print('''Selecioone o número da operação desejada: 

1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão\n''')

# Validador de opção informada
while True:
    try:
        opcao = int(input('Digite sua opção (1/2/3/4): '))
        if opcao in range(1, 5):
            break
        else:
            print(f'Valor {opcao} inválido! Digite um valor de 1 a 4.')
    except Exception as erro:
        print(f'Erro {erro.__class__}. Digite um valor de 1 a 4.')

# Validador de números inteiros informados
while True:
    try:
        valor_um = int(input('Digite o primeiro número inteiro: '))
        valor_dois = int(input('Digite o segundo número inteiro: '))
        break
    except Exception as erro:
        print(
            'Um dos valores digitados é inválido! Favor informar valores numéricos reais.')

# Funções Lambda para cada operação
def soma(x, y): return x + y
def subtracao(x, y): return x - y
def multiplicacao(x, y): return x * y
def divisao(x, y): return x / y

# Execução do resultado
if opcao == 1:
    print(f'{valor_um} + {valor_dois} = {soma(valor_um, valor_dois)}')
elif opcao == 2:
    print(f'{valor_um} - {valor_dois} = {subtracao(valor_um, valor_dois)}')
elif opcao == 3:
    print(f'{valor_um} * {valor_dois} = {multiplicacao(valor_um, valor_dois)}')
elif opcao == 4:
    print(f'{valor_um} / {valor_dois} = {divisao(valor_um, valor_dois)}')
