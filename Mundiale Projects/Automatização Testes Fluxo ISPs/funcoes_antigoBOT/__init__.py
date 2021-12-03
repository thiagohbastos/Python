from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import time, sleep

def tratar_cidade(navegador):
    try:
        navegador.find_element(By.XPATH, '//*[@id="modal-portal"]/div/div/form/div/div/select').click()
        navegador.find_element(By.XPATH, '//*[@id="modal-portal"]/div/div/form/div/div/select/option[2]').click()
        navegador.find_element(By.XPATH, '//*[@id="modal-portal"]/div/div/form/button').click()
        return 'OK'
    except:
        try:
            navegador.find_element(By.XPATH, '//*[@id="__next"]/section/div/div/main/section/div/select').click()
            navegador.find_element(By.XPATH,
                                   '//*[@id="__next"]/section/div/div/main/section/div/select/option[2]').click()
            return 'OK'
        except:
            try:
                navegador.find_element(By.XPATH, '//*[@id="modal-portal"]/div/div/form/div/div/div/select').click()
                navegador.find_element(By.XPATH,
                                       '//*[@id="modal-portal"]/div/div/form/div/div/div/select/option[2]').click()
                navegador.find_element(By.XPATH, '//*[@id="modal-portal"]/div/div/form/button').click()
                return 'OK'
            except:
                return 'N/A'
                pass


def abrir_snippet(navegador):
    try:
        sleep(1)
        navegador.execute_script('document.querySelector("#dots-cta > img").click()')  # clica snippet
        navegador.execute_script('document.querySelector("#dots-chat-cta > img").click()')  # clica no ícone webchat
        return 'OK'
    except:
        return 'Não OK'


def interacao_chat(CEP, NUMERO, navegador):
    auxiliar_2 = list()
    try:
        navegador.switch_to.frame(navegador.find_element(By.ID, 'blip-chat-iframe'))
    except Exception as erro:
        auxiliar_2.append(f'Não OK - {erro.__class__}')
    else:
        auxiliar_2.append('OK')

    auxiliar_2.append(
        esperar_enviar('//*[@id="messages-list"]/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div',
                       'msg-textarea', 'Não', 10, navegador))

    auxiliar_2.append(
        esperar_enviar('//*[@id="messages-list"]/div[1]/div/div/div[2]/div[4]/div[2]/div[2]/div/div/div/div/div[1]/div',
                       'msg-textarea', CEP, 10, navegador))

    auxiliar_2.append(
        esperar_enviar('//*[@id="messages-list"]/div[1]/div/div/div[2]/div[6]/div[2]/div[1]/div/div/div/div/div[1]/div',
                       'msg-textarea', NUMERO, 10, navegador))

    auxiliar_2.append(esperar_enviar(
        '//*[@id="messages-list"]/div[1]/div/div/div[2]/div[8]/div[2]/div[1]/div/div/div/div/div[1]/div[1]',
        'msg-textarea', 'sim', 10, navegador))

    auxiliar_2.append(esperar_enviar(
        '//*[@id="messages-list"]/div[1]/div/div/div[2]/div[10]/div[2]/div[2]/div/div/div/div/div[1]/div',
        'msg-textarea', 'Favor encerrar como teste. Tenha um ótimo trabalho! 😁', 40, navegador))
    return auxiliar_2[:]


def url_lps():
    sites = {'EVA': {'BLINK': ['https://ofertasblinktelecom.com.br/', 31235060, 148],
                     'BRISANET': ['https://ofertasbrisanet.com.br', 55012640, 13]
                     'TELY': ['https://ofertastely.com.br/', 58038000, 315],
                     'LIGUE': ['https://ofertasligue.net/', 87005002, 405],
                     'SUMICITY': ['https://ofertassumicity.com.br/', 27534240, 382],
                     'VIP': ['https://ofertasvipbrtelecom.com.br/', '09415110', 16]
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
                     'COPEL': ['https://ofertascopeltelecom.com.br/', 99010220, 36],
                     'ALGAR': ['https://ofertasalgartelecom.com.br/', 99010220, 36]}}
    return sites.copy()


def esperar_enviar(elemento_procurado, id_html_mensagem, mensagem, tempo_espera, navegador):
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