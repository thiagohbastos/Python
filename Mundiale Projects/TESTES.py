import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import time, sleep
import datetime

navegador = webdriver.Chrome()

def cidade():
    try:
        navegador.find_element(By.XPATH, '//*[@id="modal-portal"]/div/div/form/div/div/select').click()
        navegador.find_element(By.XPATH, '//*[@id="modal-portal"]/div/div/form/div/div/select/option[2]').click()
        navegador.find_element(By.XPATH, '//*[@id="modal-portal"]/div/div/form/button').click()
        return 'Cidade escolhida: OK'
    except:
        try:
            navegador.find_element(By.XPATH, '//*[@id="__next"]/section/div/div/main/section/div/select').click()
            navegador.find_element(By.XPATH,
                '//*[@id="__next"]/section/div/div/main/section/div/select/option[2]').click()
            return 'Cidade escolhida: OK'
        except:
            try:
                navegador.find_element(By.XPATH, '//*[@id="modal-portal"]/div/div/form/div/div/div/select').click()
                navegador.find_element(By.XPATH,
                    '//*[@id="modal-portal"]/div/div/form/div/div/div/select/option[2]').click()
                navegador.find_element(By.XPATH, '//*[@id="modal-portal"]/div/div/form/button').click()
                return 'Cidade escolhida: OK'
            except:
                return 'Não há escolha.'
                pass


def abrir_chat():
    sleep(1)
    navegador.execute_script('document.querySelector("#dots-cta > img").click()')  # clica snippet
    navegador.execute_script('document.querySelector("#dots-chat-cta > img").click()')  # clica no ícone webchat


def esperar_enviar(elemento_procurado, id_html_mensagem, mensagem, tempo_espera):
    start = time()

    try:
        WebDriverWait(navegador, tempo_espera).until(
            expected_conditions.presence_of_element_located((By.XPATH, elemento_procurado)))
        sleep(1)
        navegador.find_element(By.ID, id_html_mensagem).send_keys(mensagem, Keys.ENTER)
        tempo_processo = float(f'{(time() - start):.2f}')

    except Exception as erro:
        return f"{erro.__class__} - Tempo superior a {tempo_espera}s na etapa."
    else:
        return tempo_processo


def interacao_chat():
    tempos = list()
    try:
        navegador.switch_to.frame(navegador.find_element(By.ID, 'blip-chat-iframe'))
    except Exception as erro:
         tempos.append(f'{erro.__class__}')
    else:
        tempos.append('OK')

    tempos.append(esperar_enviar('//*[@id="messages-list"]/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div',
                   'msg-textarea', 'Não', 10))

    tempos.append(esperar_enviar('//*[@id="messages-list"]/div[1]/div/div/div[2]/div[4]/div[2]/div[2]/div/div/div/div/div[1]/div',
                   'msg-textarea', '99010220', 10))

    tempos.append(esperar_enviar('//*[@id="messages-list"]/div[1]/div/div/div[2]/div[6]/div[2]/div[1]/div/div/div/div/div[1]/div',
                   'msg-textarea', '36', 10))

    tempos.append(esperar_enviar('//*[@id="messages-list"]/div[1]/div/div/div[2]/div[8]/div[2]/div[1]/div/div/div/div/div[1]/div[1]',
                   'msg-textarea', 'sim', 10))

    tempos.append(esperar_enviar('//*[@id="messages-list"]/div[1]/div/div/div[2]/div[10]/div[2]/div[1]/div/div/div/div/div[1]/div',
                   'msg-textarea', 'Favor encerrar como teste. Tenha um ótimo trabalho! :)', 60))
    return tempos[:]


# LISTA com LPs
sites = {'EVA':{'BLINK':'https://ofertasblinktelecom.com.br/',
          'BRISANET':'https://ofertasbrisanet.com.br',
          'TELY':'https://ofertastely.com.br/',
          'LIGUE':'https://ofertasligue.net/',
          'SUMICITY':'https://ofertassumicity.com.br/',
          'VIP':'https://ofertasvipbrtelecom.com.br/'},

         'WALL-E':{'TVN':'https://ofertastvn.com.br',
          'COPREL':'http://ofertascoprel.com.br/',
          'NOVA FIBRA':'https://ofertasnova.com.br',
          'DESKTOP':'https://ofertasdesktop.com.br',
          'MASTER':'https://ofertassoumaster.com.br/',
          'AZZA':'https://ofertasazza.net.br/',
          'FLEETNET':'https://ofertasfleetnet.com.br/',
          'SOCITEL':'https://mkt.azza.net.br/socitel'},

         'BURN-E':{'MOB':'http://ofertasmobtelecom.com.br/',
          'WECLIX':'http://ofertasweclix.com.br',
          'CABONNET':'https://ofertascabonnet.com.br/',
          'SERCOMTEL':'http://ofertasercomtel.com.br/',
          'PROXXIMA':'https://ofertastoolsnet.com.br/'},

         'M-O':{'VALENET':'https://ofertasvalenet.com.br/',
          'INFOVALE':'http://ofertasinfovaletelecom.com.br/',
          'COPEL':'https://ofertascopeltelecom.com.br/'}}


while True:
    print('''Realizar testes para qual Squad?
0 - Todos os Squads das ISPs
1 - EVA
2 - WALL-e
3 - BURN-e
4 - M-O''')
    resp = int(input('Opção: '))
    if resp in range (0, 5):
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
            if sites[k] == 'EVA':
                navegador.get(lp)
            else:
                navegador.switch_to.new_window('tab')
                navegador.get(lp)
            cidade()
            abrir_chat()
            resultado[k2] = interacao_chat()

else:
    for k2, lp in sites[resp].items():
        navegador.switch_to.new_window('tab')
        navegador.get(lp)
        cidade()
        abrir_chat()
        resultado[k2] = interacao_chat()

df = pd.DataFrame(data=resultado, index=['Abrir CHAT', 'Já sou cliente', 'CEP', 'Nº', 'Confirmação', 'Transbordo'])
df.to_excel(f'Teste de Fluxo - {resp}.xlsx', sheet_name=f'{datetime.date.today()}')
