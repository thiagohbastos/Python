import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import time, sleep
import datetime

def cidade():
    try:
        navegador.find_element(By.XPATH, '//*[@id="modal-portal"]/div/div/form/div/div/select').click()
        navegador.find_element(By.XPATH, '//*[@id="modal-portal"]/div/div/form/div/div/select/option[2]').click()
        navegador.find_element(By.XPATH, '//*[@id="modal-portal"]/div/div/form/button').click()
        tempos.append('OK')
    except:
        try:
            navegador.find_element(By.XPATH, '//*[@id="__next"]/section/div/div/main/section/div/select').click()
            navegador.find_element(By.XPATH,
                                   '//*[@id="__next"]/section/div/div/main/section/div/select/option[2]').click()
            tempos.append('OK')
        except:
            try:
                navegador.find_element(By.XPATH, '//*[@id="modal-portal"]/div/div/form/div/div/div/select').click()
                navegador.find_element(By.XPATH,
                                       '//*[@id="modal-portal"]/div/div/form/div/div/div/select/option[2]').click()
                navegador.find_element(By.XPATH, '//*[@id="modal-portal"]/div/div/form/button').click()
                tempos.append('OK')
            except:
                tempos.append('N/A')
                pass


def abrir_snippet():
    try:
        sleep(1)
        navegador.execute_script('document.querySelector("#dots-cta > img").click()')  # clica snippet
        navegador.execute_script('document.querySelector("#dots-chat-cta > img").click()')  # clica no ícone webchat
        tempos.append('OK')
    except:
        tempos.append('Não OK')


def esperar_enviar(elemento_procurado, id_html_mensagem, mensagem, tempo_espera):
    start = time()

    try:
        WebDriverWait(navegador, tempo_espera).until(
            expected_conditions.presence_of_element_located((By.XPATH, elemento_procurado)))
        sleep(1)
        navegador.find_element(By.ID, id_html_mensagem).send_keys(mensagem, Keys.ENTER)
        tempo_processo = float(f'{(time() - start):.2f}')

    except Exception as erro:
        return f"Não OK (superior a {tempo_espera}s)"
    else:
        return tempo_processo


def interacao_chat(CEP, NUMERO):
    try:
        navegador.switch_to.frame(navegador.find_element(By.ID, 'blip-chat-iframe'))
    except Exception as erro:
        tempos.append(f'Não OK - {erro.__class__}')
    else:
        tempos.append('OK')

    tempos.append(
        esperar_enviar('//*[@id="messages-list"]/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div',
                       'msg-textarea', 'Não', 10))

    tempos.append(
        esperar_enviar('//*[@id="messages-list"]/div[1]/div/div/div[2]/div[4]/div[2]/div[2]/div/div/div/div/div[1]/div',
                       'msg-textarea', CEP, 10))

    tempos.append(
        esperar_enviar('//*[@id="messages-list"]/div[1]/div/div/div[2]/div[6]/div[2]/div[1]/div/div/div/div/div[1]/div',
                       'msg-textarea', NUMERO, 10))

    tempos.append(esperar_enviar(
        '//*[@id="messages-list"]/div[1]/div/div/div[2]/div[8]/div[2]/div[1]/div/div/div/div/div[1]/div[1]',
        'msg-textarea', 'sim', 1))

    tempos.append(esperar_enviar(
        '//*[@id="messages-list"]/div[1]/div/div/div[2]/div[10]/div[2]/div[2]/div/div/div/div/div[1]/div',
        'msg-textarea', 'Favor encerrar como teste. Tenha um ótimo trabalho! :)', 30))
    return tempos[:]


navegador = webdriver.Chrome()

# LISTA com LPs
sites = {'EVA': {'BLINK': ['https://ofertasblinktelecom.com.br/', 99010220, 36],
                 'BRISANET': ['https://ofertasbrisanet.com.br', 99010220, 36],
                 'TELY': ['https://ofertastely.com.br/', 99010220, 36],
                 'LIGUE': ['https://ofertasligue.net/', 99010220, 36],
                 'SUMICITY': ['https://ofertassumicity.com.br/', 99010220, 36],
                 'VIP': ['https://ofertasvipbrtelecom.com.br/', 99010220, 36]
                 },

         'WALL-E': {'TVN': ['https://ofertastvn.com.br', 99010220, 36],
                    'COPREL': ['http://ofertascoprel.com.br/', 99010220, 36],
                    'NOVA FIBRA': ['https://ofertasnova.com.br', 99010220, 36],
                    'DESKTOP': ['https://ofertasdesktop.com.br', 99010220, 36],
                    'MASTER': ['https://ofertassoumaster.com.br/', 99010220, 36],
                    'AZZA': ['https://ofertasazza.net.br/', 99010220, 36],
                    'FLEETNET': ['https://ofertasfleetnet.com.br/', 99010220, 36],
                    'SOCITEL': ['https://mkt.azza.net.br/socitel', 99010220, 36]},

         'BURN-E': {'MOB': ['http://ofertasmobtelecom.com.br/', 99010220, 36],
                    'WECLIX': ['http://ofertasweclix.com.br', 99010220, 36],
                    'CABONNET': ['https://ofertascabonnet.com.br/', 99010220, 36],
                    'SERCOMTEL': ['http://ofertasercomtel.com.br/', 99010220, 36],
                    'PROXXIMA': ['https://ofertastoolsnet.com.br/', 99010220, 36]},

         'M-O': {'VALENET': ['https://ofertasvalenet.com.br/', 99010220, 36],
                 'INFOVALE': ['http://ofertasinfovaletelecom.com.br/', 99010220, 36],
                 'COPEL': ['https://ofertascopeltelecom.com.br/', 99010220, 36]}}

tempos = list()

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
                tempos.append('Fora do Ar')
                continue
            else:
                tempos.append('OK')
                c = sites[k][k2][1]
                n = sites[k][k2][2]
                cidade()
                abrir_snippet()
                resultado[k2] = interacao_chat(c, n)
                tempos.clear()

else:
    for k2, lp in sites[resp].items():
        try:
            if k2 in 'BLINK TVN MOB VALENET':
                navegador.get(lp[0])
            else:
                navegador.switch_to.new_window('tab')
                navegador.get(lp[0])
        except:
            tempos.append('Fora do Ar')
        else:
            tempos.append('OK')
            cidade()
            abrir_snippet()
            c = sites[resp][k2][1]
            n = sites[resp][k2][2]
            resultado[k2] = interacao_chat(c, n)
            tempos.clear()

df = pd.DataFrame(data=resultado,
                  index=['Carregamento LP', 'Seleciona Cidade', 'SNIPPET', 'IFRAME', 'Já sou cliente', 'CEP', 'Nº',
                         'Confirmação', 'Transbordo'])
df.to_excel(f'Teste de Fluxo - {resp}.xlsx', sheet_name=f'{datetime.date.today()}')
