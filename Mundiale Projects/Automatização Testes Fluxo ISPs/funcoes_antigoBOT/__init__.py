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
    global auxiliar
    auxiliar = list()
    try:
        navegador.switch_to.frame(navegador.find_element(By.ID, 'blip-chat-iframe'))
    except Exception as erro:
        auxiliar.append(f'Não OK - {erro.__class__}')
    else:
        auxiliar.append('OK')

    auxiliar.append(
        esperar_enviar('//*[@id="messages-list"]/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div',
                       'msg-textarea', 'Não', 10, navegador))

    auxiliar.append(
        esperar_enviar('//*[@id="messages-list"]/div[1]/div/div/div[2]/div[4]/div[2]/div[2]/div/div/div/div/div[1]/div',
                       'msg-textarea', CEP, 10, navegador))

    auxiliar.append(
        esperar_enviar('//*[@id="messages-list"]/div[1]/div/div/div[2]/div[6]/div[2]/div[1]/div/div/div/div/div[1]/div',
                       'msg-textarea', NUMERO, 10, navegador))

    auxiliar.append(esperar_enviar(
        '//*[@id="messages-list"]/div[1]/div/div/div[2]/div[8]/div[2]/div[1]/div/div/div/div/div[1]/div[1]',
        'msg-textarea', 'sim', 10, navegador))

    auxiliar.append(esperar_enviar(
        '//*[@id="messages-list"]/div[1]/div/div/div[2]/div[10]/div[2]/div[2]/div/div/div/div/div[1]/div',
        'msg-textarea', 'Favor encerrar como teste. Tenha um ótimo trabalho! 😁', 30, navegador))
    return auxiliar[:]


def url_lps():
    sites = {'EVA': {'BLINK': ['https://ofertasblinktelecom.com.br/', 31235060, 148],
                     'BRISANET': ['https://ofertasbrisanet.com.br', 55012640, 13],
                     'TELY': ['https://ofertastely.com.br/', 58038000, 315],
                     'LIGUE': ['https://ofertasligue.net/', 87005002, 405],
                     'SUMICITY': ['https://ofertassumicity.com.br/', 27534240, 382],
                     'VIP': ['https://ofertasvipbrtelecom.com.br/', '09415110', 16]
                     },

             'WALL-E': {'TVN': ['https://ofertastvn.com.br', 99010220, 36],
                        #'COPREL': ['http://ofertascoprel.com.br/', 99010220, 36],
                        #'NOVA FIBRA': ['https://ofertasnova.com.br', 99010220, 36],
                        #'DESKTOP': ['https://ofertasdesktop.com.br', 99010220, 36],
                        #'MASTER': ['https://ofertassoumaster.com.br/', 99010220, 36],
                        #'AZZA': ['https://ofertasazza.net.br/', 99010220, 36],
                        #'FLEETNET': ['https://ofertasfleetnet.com.br/', 99010220, 36],
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


def mapeamento_steps():
    palavras_chave = {'ERRO1': ['Ocorreu um erro'],
                      'ERRO2': ['Não entendi'],
                      'Consultor Indisponível': ['Os nossos consultores estão disponíveis das'],
                      'Já sou Cliente': ['Você já é nosso cliente?', 'Não'],
                      'Condominio': ['localizado em um condomínio', 'Não'],
                      'CEP': ['digite o seu CEP', cep],
                      'Número Ende.': ['digite o número do endereço', numero],
                      'Complemento': ['o complemento do endereço', não],
                      'Confirma endereço': ['Está correto?', 'Sim'],
                      'Oferta Planos': ['Vamos escolher o melhor plano', 1],
                      'Dados': ['nome completo', 'Teste Fluxo Completo'],
                      'CPF': ['Me diga o seu CPF', 11111111111],
                      'RG': ['número do seu RG', 00000000],
                      'Data Nascimento': ['data de nascimento', '01/01/2000'],
                      'Nome Mãe': ['nome da sua mãe', 'Teste Nome Mãe'],
                      'Gênero': ['me informe o seu gênero', 'Não binário'],
                      'Estado Civil': ['estado civil', 'Solteiro'],
                      'Telefone': ['número preferível', '31955555555'],
                      'Telefone 2': ['número adicional','31966666666'],
                      'E-mail': ['e-mail para o cadastro', 'nulonulo@gmail.com'],
                      'Turno Inst.': ['o turno ideal para a instalação', 'Tarde'],
                      'Confirma Pedido': ['Preciso que você confirme as seguintes informações', 'Não Confirmo'],
                      'Motivo não confirmação': ['Você não confirmou por qual motivo?', 'Falar com humano'],
                      'Transbordo ATH': ['Aguarde só um momento, estou verificando a disponibilidade', 'Favor finalizar como teste. Tenha um ótimo trabalho! 😁'],
                      }
    return palavras_chave.copy()


def encontra_msg(navegador):
    steps = mapeamento_steps()
    while True:
        n_bloco_atual = len(navegador.find_elements(By.XPATH, '//*[@id="messages-list"]/div[1]/div/div/div[2]/div'))
        try:
            WebDriverWait(navegador, 2).until(
                expected_conditions.presence_of_element_located((By.XPATH, f'//*[@id="messages-list"]/div[1]/div/div/div[2]/div[{n_bloco_atual+1}]')))
        except:
            break
        else:
            continue
    n_ultima_msg = len(navegador.find_elements(By.XPATH,
                                               f'//*[@id="messages-list"]/div[1]/div/div/div[2]/div[{n_bloco_atual}]/div[2]/div'))
    for cont in range(1, n_ultima_msg + 1):
        mensagem = navegador.find_element(By.XPATH,
                                            f'//*[@id="messages-list"]/div[1]/div/div/div[2]/div[{n_bloco_atual}]/div[2]/div[{cont}]/div/div/div/div/div[1]/div[1]').text
        for key, valor in steps.items():
            if valor[0] in mensagem:
                return key


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