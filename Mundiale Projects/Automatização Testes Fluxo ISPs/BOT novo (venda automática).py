import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from funcoes_novoBOT import tratar_cidade, abrir_snippet, url_lps, interacao_chat
import datetime

navegador = webdriver.Chrome()
sites = url_lps()
resultado_etapas = []
resultado_geral = dict()
lista_auxiliar = []
tamanho_maximo_etapas = 0

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

if resp == 0:
    for k, squad in sites.items():
        for k2, lp in squad.items():
            print(f'Estou iniciando os testes na \033[1:34m{k2}\033[m.')
            resultado_geral[k2] = []
            try:
                if sites[k][k2][0] == 'https://ofertasblinktelecom.com.br/':
                    navegador.get(lp[0])
                else:
                    navegador.switch_to.new_window('tab')
                    navegador.get(lp[0])
            except:
                resultado_geral[k2] = 'LP Fora do Ar'
                print('Teste finalizado com falha no carregamento da LP!')
                print('\033[1:33m-' * 40, end='\033[m\n')
                continue
            else:
                c = sites[k][k2][1]
                n = sites[k][k2][2]
                resultado_etapas.append('LP OK')
                resultado_etapas.append(tratar_cidade(navegador))
                resultado_etapas.append(abrir_snippet(navegador))
                try:
                    navegador.switch_to.frame(navegador.find_element(By.ID, 'blip-chat-iframe'))
                except:
                    resultado_etapas.append('CHAT não OK.')
                    for cont in range(0, len(lista_auxiliar)):
                        resultado_etapas.append(lista_auxiliar[cont])
                    continue
                else:
                    resultado_etapas.append('CHAT OK')

                lista_auxiliar = interacao_chat(navegador, c, n)

                for cont in range(0, len(lista_auxiliar)):
                    resultado_etapas.append(lista_auxiliar[cont])
                resultado_geral[k2] = resultado_etapas[:]
                resultado_etapas.clear()
                lista_auxiliar.clear()
                print('Teste finalizado com êxito!')
                print('\033[1:33m-' * 40, end='\033[m\n')

else:
    for k2, lp in sites[resp].items():
        resultado_geral[k2] = []
        try:
            print(f'Estou iniciando os testes na \033[1:34m{k2}\033[m.')
            if k2 in 'BLINK TVN MOB VALENET':
                navegador.get(lp[0])
            else:
                navegador.switch_to.new_window('tab')
                navegador.get(lp[0])
        except:
            resultado_geral[k2] = 'LP Fora do Ar'
            print('Teste finalizado com falha no carregamento da LP!')
            print('\033[1:33m-' * 40, end='\033[m\n')
        else:
            c = sites[resp][k2][1]
            n = sites[resp][k2][2]
            resultado_etapas.append('LP OK')
            resultado_etapas.append(tratar_cidade(navegador))
            resultado_etapas.append(abrir_snippet(navegador))

            try:
                navegador.switch_to.frame(navegador.find_element(By.ID, 'blip-chat-iframe'))
            except:
                resultado_etapas.append('CHAT não OK.')
                continue
            else:
                resultado_etapas.append('CHAT OK')

            lista_auxiliar = interacao_chat(navegador, c, n)
            for cont in range(0, len(lista_auxiliar)):
                resultado_etapas.append(lista_auxiliar[cont])

            resultado_geral[k2] = resultado_etapas[:]
            resultado_etapas.clear()
            lista_auxiliar.clear()
            print('Teste finalizado com êxito!')
            print('\033[1:33m-' * 40, end='\033[m\n')

for key, valor in resultado_geral.items():
    if len(valor) > tamanho_maximo_etapas:
        tamanho_maximo_etapas = len(valor)

for key, valor in resultado_geral.items():
    if len(valor) < tamanho_maximo_etapas:
        dif = tamanho_maximo_etapas - len(valor)
        for cont in range(0, dif):
            valor.append('-')

df = pd.DataFrame(data=resultado_geral)
df.to_excel(f'Teste de Fluxo - {resp}.xlsx', sheet_name=f'{datetime.date.today()}')

