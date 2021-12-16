import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from funcoes_novoBOT import tratar_cidade, abrir_snippet, url_lps, interacao_chat
import datetime

navegador = webdriver.Chrome()
sites = url_lps()
resultado_etapas = []
resultado_geral = dict()
lista_auxiliar = []

while True:
    print('''Realizar testes para qual Squad?
0 - Todos os Squads
1 - EVA
2 - WALL-e
3 - BURN-e
4 - M-O''')
    resp = int(input('Opção: '))
    if resp in range(0, 5):
        break
    print('\033[1:31mOpção inválida!\033[m')
while True:
    salvar = str(input('\nGostaria de salvar os resultados em arquivo xlsx? [S/N] ')).upper().strip()
    if salvar in 'SN':
        break
    else:
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
            print('\033[1:33m-' * 40, end='\033[m\n')
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
                continue
            else:
                c = sites[k][k2][1]
                n = sites[k][k2][2]
                venci = 'Não sei'
                try:
                    venci = sites[k][k2][3]
                except:
                    pass
                resultado_etapas.append('LP OK')
                resultado_etapas.append(tratar_cidade(navegador))
                resultado_etapas.append(abrir_snippet(navegador))
                try:
                    navegador.switch_to.frame(navegador.find_element(By.ID, 'blip-chat-iframe'))
                    WebDriverWait(navegador, 30).until(
                        expected_conditions.presence_of_element_located(
                            (By.XPATH, '//*[@id="messages-list"]/div[1]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div[1]/div')))
                except:
                    resultado_etapas.append('CHAT TIMEOUT')
                    for cont in range(0, len(lista_auxiliar)):
                        resultado_etapas.append(lista_auxiliar[cont])
                    continue
                else:
                    resultado_etapas.append('CHAT OK')

                lista_auxiliar = interacao_chat(navegador, k2, c, n, venci)
                for cont in range(0, len(lista_auxiliar)):
                    resultado_etapas.append(lista_auxiliar[cont])

                resultado_geral[k2] = resultado_etapas[:]
                resultado_etapas.clear()
                lista_auxiliar.clear()
                print('Teste finalizado com êxito!')

        tamanho_maximo_etapas = 0
        for operacao in resultado_geral.values():
            if len(operacao) > tamanho_maximo_etapas:
                tamanho_maximo_etapas = len(operacao)

        for operacao in resultado_geral.values():
            if len(operacao) < tamanho_maximo_etapas:
                dif = tamanho_maximo_etapas - len(operacao)
                for cont in range(0, dif):
                    operacao.append('-')

        vars()[f'df_{k}'] = pd.DataFrame(data=resultado_geral)
        resultado_geral.clear()

else:
    for k2, lp in sites[resp].items():
        resultado_geral[k2] = []
        try:
            print('\033[1:33m-' * 40, end='\033[m\n')
            print(f'Estou iniciando os testes na \033[1:34m{k2}\033[m.')
            if k2 in 'BLINK TVN MOB VALENET':
                navegador.get(lp[0])
            else:
                navegador.switch_to.new_window('tab')
                navegador.get(lp[0])
        except:
            resultado_geral[k2] = 'LP Fora do Ar'
            print('Teste finalizado com falha no carregamento da LP!')
        else:
            c = sites[resp][k2][1]
            n = sites[resp][k2][2]
            venci = 'Não sei'
            try:
                venci = sites[resp][k2][3]
            except:
                pass
            resultado_etapas.append('LP OK')
            resultado_etapas.append(tratar_cidade(navegador))
            resultado_etapas.append(abrir_snippet(navegador))

            try:
                navegador.switch_to.frame(navegador.find_element(By.ID, 'blip-chat-iframe'))
                WebDriverWait(navegador, 30).until(
                    expected_conditions.presence_of_element_located(
                        (By.XPATH,
                         '//*[@id="messages-list"]/div[1]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div[1]/div')))
            except:
                resultado_etapas.append('CHAT TIMEOUT')
                continue
            else:
                resultado_etapas.append('CHAT OK')

            lista_auxiliar = interacao_chat(navegador, k2, c, n, venci)
            for cont in range(0, len(lista_auxiliar)):
                resultado_etapas.append(lista_auxiliar[cont])

            resultado_geral[k2] = resultado_etapas[:]
            resultado_etapas.clear()
            lista_auxiliar.clear()
            print('Teste finalizado com êxito!')

    tamanho_maximo_etapas = 0
    for operacao in resultado_geral.values():
        if len(operacao) > tamanho_maximo_etapas:
            tamanho_maximo_etapas = len(operacao)

    for operacao in resultado_geral.values():
        if len(operacao) < tamanho_maximo_etapas:
            dif = tamanho_maximo_etapas - len(operacao)
            for cont in range(0, dif):
                operacao.append('-')

    vars()[f'df_{resp}'] = pd.DataFrame(data=resultado_geral)
    resultado_geral.clear()

hora = int(str(datetime.datetime.time(datetime.datetime.today()))[:2])
if 12 > hora >= 6:
    turno = 'Manhã'
elif 18 > hora >= 12:
    turno = 'Tarde'
else:
    turno = 'Noite'

if salvar == 'S':
    arquivo = pd.ExcelWriter(
        f'S:/Inovação/Planejamento/3 - MIS/Gerencial/Acompanhamento das ISPS - Semanal/Testes de Fluxo/'
        f'Testes de Fluxo {datetime.date.today().day}-{datetime.date.today().month} ({turno}).xlsx', engine='xlsxwriter')
    if resp == 0:
        for k, squad in sites.items():
            vars()[f'df_{k}'].to_excel(arquivo, sheet_name=k, index=False)
    else:
        vars()[f'df_{resp}'].to_excel(arquivo, sheet_name=resp, index=False)
    arquivo.save()
