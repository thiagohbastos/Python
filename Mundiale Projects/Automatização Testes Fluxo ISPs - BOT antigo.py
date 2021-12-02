import pandas as pd
from selenium import webdriver
import datetime
from funcoes_antigoBOT import tratar_cidade, abrir_snippet, interacao_chat, url_lps

navegador = webdriver.Chrome()

sites = url_lps()

auxiliar = list()

while True:
    print('''Realizar testes para qual Squad?
0 - Todos os Squads das ISPs
1 - EVA
2 - WALL-e
3 - BURN-e
4 - M-O''')
    resp = int(input('Opção: '))
    if resp in range(0, 5):
        break
    print('\033[1:31mOpção inválida!\033[m')

if resp == 1:
    resp = 'EVA'
elif resp == 2:
    resp = 'WALL-E'
elif resp == 3:
    resp = 'BURN-E'
elif resp == 4:
    resp = 'M-O'

resultado = dict()

if resp == 0:
    for k, squad in sites.items():
        for k2, lp in squad.items():
            try:
                if sites[k][k2][0] == 'https://ofertasblinktelecom.com.br/':
                    navegador.get(lp[0])
                else:
                    navegador.switch_to.new_window('tab')
                    navegador.get(lp[0])
            except:
                auxiliar.append('Fora do Ar')
                continue
            else:
                c = sites[k][k2][1]
                n = sites[k][k2][2]
                auxiliar.append('OK')
                auxiliar.append(tratar_cidade(navegador))
                auxiliar.append(abrir_snippet(navegador))
                tps_interacao = interacao_chat(c, n, navegador)
                for cont in range(0, len(tps_interacao)):
                    auxiliar.append(tps_interacao[cont])
                resultado[k2] = auxiliar[:]
                auxiliar.clear()

else:
    for k2, lp in sites[resp].items():
        try:
            if k2 in 'BLINK TVN MOB VALENET':
                navegador.get(lp[0])
            else:
                navegador.switch_to.new_window('tab')
                navegador.get(lp[0])
        except:
            auxiliar.append('Fora do Ar')
            continue
        else:
            c = sites[resp][k2][1]
            n = sites[resp][k2][2]
            auxiliar.append('OK')
            auxiliar.append(tratar_cidade(navegador))
            auxiliar.append(abrir_snippet(navegador))
            tps_interacao = interacao_chat(c, n, navegador)
            for cont in range(0, len(tps_interacao)):
                auxiliar.append(tps_interacao[cont])
            resultado[k2] = auxiliar[:]
            auxiliar.clear()

df = pd.DataFrame(data=resultado,
                  index=['Carregamento LP', 'Seleciona Cidade', 'SNIPPET', 'IFRAME', 'Já sou cliente', 'CEP', 'Nº',
                         'Confirmação', 'Transbordo'])
df.to_excel(f'Teste de Fluxo - {resp}.xlsx', sheet_name=f'{datetime.date.today()}')
