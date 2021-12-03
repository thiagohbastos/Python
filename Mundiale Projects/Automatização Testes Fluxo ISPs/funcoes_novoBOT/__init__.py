from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import time, sleep


# Defs antigas:
def tratar_cidade(navegador):
    try:
        navegador.find_element(By.XPATH, '//*[@id="modal-portal"]/div/div/form/div/div/select').click()
        navegador.find_element(By.XPATH, '//*[@id="modal-portal"]/div/div/form/div/div/select/option[2]').click()
        navegador.find_element(By.XPATH, '//*[@id="modal-portal"]/div/div/form/button').click()
        return 'Cidade OK'
    except:
        try:
            navegador.find_element(By.XPATH, '//*[@id="__next"]/section/div/div/main/section/div/select').click()
            navegador.find_element(By.XPATH,
                                   '//*[@id="__next"]/section/div/div/main/section/div/select/option[2]').click()
            return 'Cidade OK'
        except:
            try:
                navegador.find_element(By.XPATH, '//*[@id="modal-portal"]/div/div/form/div/div/div/select').click()
                navegador.find_element(By.XPATH,
                                       '//*[@id="modal-portal"]/div/div/form/div/div/div/select/option[2]').click()
                navegador.find_element(By.XPATH, '//*[@id="modal-portal"]/div/div/form/button').click()
                return 'Cidade OK'
            except:
                return 'N/A'
                pass


def abrir_snippet(navegador):
    try:
        sleep(1)
        navegador.execute_script('document.querySelector("#dots-cta > img").click()')  # clica snippet
        navegador.execute_script('document.querySelector("#dots-chat-cta > img").click()')  # clica no ícone webchat
        return 'Snippet OK'
    except:
        return 'Snippet Não OK'


# Defs Novas:
def url_lps():
    sites = {'EVA': {'BLINK': ['https://ofertasblinktelecom.com.br/', '31235060', '148'],
                     'BRISANET': ['https://ofertasbrisanet.com.br', '59607571', '241'],
                     'TELY': ['https://ofertastely.com.br/', '58038000', '315'],
                     'LIGUE': ['https://ofertasligue.net/', '87005002', '405'],
                     'SUMICITY': ['https://ofertassumicity.com.br/', '27534240', '382'],
                     'VIP': ['https://ofertasvipbrtelecom.com.br/', '09415110', '16']
                     },

             'WALL-E': {'TVN': ['https://ofertastvn.com.br', '65130000', '325'],
                        'COPREL': ['http://ofertascoprel.com.br/', '98280000', '175'],
                        'DESKTOP': ['https://ofertasdesktop.com.br', '11712020', '315'],
                        'MASTER': ['https://ofertassoumaster.com.br/', '38616072', '22'],
                        'AZZA': ['https://ofertasazza.net.br/', '18071724', '65'],
                        'FLEETNET': ['https://ofertasfleetnet.com.br/', '19026410', '885'],
                        'SOCITEL': ['https://mkt.azza.net.br/socitel', '06770300', '350']},

             'BURN-E': {'MOB': ['http://ofertasmobtelecom.com.br/', '60525200', '150'],
                        'WECLIX': ['http://ofertasweclix.com.br', '14807049', '60'],
                        'CABONNET': ['https://ofertascabonnet.com.br/', '19042410', '347'],
                        'SERCOMTEL': ['http://ofertasercomtel.com.br/', '86055630', '995'],
                        'PROXXIMA': ['https://ofertastoolsnet.com.br/', '59575000', '07']},

             'M-O': {'VALENET': ['https://ofertasvalenet.com.br/', '31930560', '120'],
                     #'INFOVALE': ['http://ofertasinfovaletelecom.com.br/', '11925000', '710'],
                     'COPEL': ['https://ofertascopeltelecom.com.br/', '87013937', '2946'],
                     'ALGAR': ['https://ofertasalgartelecom.com.br/', '38407261', '295'],
                     'MHNET': ['https://ofertasmhnet.com.br/', '84032602', '34']
                     }}
    return sites.copy()


def mapeamento_steps(cep, numero):
    palavras_chave = {'ERRO1': ['Ocorreu um erro'],
                      'ERRO2': ['Não entendi'],
                      'Consultor Indisponível': ['Os nossos consultores estão disponíveis das'],
                      'Finalização': ['Estamos finalizando o seu atendimento'],
                      'Já sou Cliente': ['Você já é nosso cliente?', 'Não'],
                      'Condominio': ['localizado em um condomínio', 'Não'],
                      'CEP': ['digite o seu CEP', cep],
                      'Número Ende.': ['o número do endereço', numero],
                      'Complemento': ['o complemento do endereço', 'não'],
                      'Referência': ['qual o ponto de referência do endereço', 'Não'],
                      'Bairro': ['nome do bairro', 'NuloNulo'],
                      'Rua': ['o nome da rua', 'NuloNulo'],
                      'Confirma endereço': ['Está correto?', 'Sim'],
                      'Oferta Planos': ['Vamos escolher o melhor plano', 1],
                      'TV': ['adicionar TV ao seu carrinho', 'Não'],
                      'Tel Fixo': ['adicionar Telefone Fixo ao seu carrinho', 'Não'],
                      'Nome': ['me informe seu nome completo', 'Teste Fluxo Completo'],
                      'CPF': ['Me diga o seu CPF', '96315157459'],
                      'RG': ['número do seu RG', '00000000'],
                      'Data Nascimento': ['data de nascimento', '01/01/2000'],
                      'Nome Mãe': ['nome da sua mãe', 'Teste Nome Mãe'],
                      'Gênero': ['me informe o seu gênero', 'Não binário'],
                      'Estado Civil': ['estado civil', 'Solteiro'],
                      'Telefone': ['número preferível', '31955555555'],
                      'Telefone 2': ['número adicional', '31966666666'],
                      'E-mail': ['e-mail para o cadastro', 'nulonulo@gmail.com'],
                      'Promoção': ['outra operadora de internet', 'Não'],
                      'Pagamento': ['pagamento por boleto digital ou por débito em conta', 'Boleto Digital'],
                      'Pagamento2': ['Qual o melhor método de pagamento pra você?', 'Boleto Online'],
                      'Turno Inst.': ['o turno ideal para a instalação', 'Tarde'],
                      'Confirma Pedido': ['Preciso que você confirme as seguintes informações', 'Não Confirmo'],
                      'Confirma Pedido2': ['Você confirma as informações acima?', 'Não Confirmo'],
                      'Motivo não confirmação': ['Você não confirmou por qual motivo?', 'Falar com humano'],
                      'Transbordo ATH': ['um consultor especializado',
                                         'Favor finalizar como teste. Tenha um ótimo trabalho!'],
                      'Transbordo ATH2': ['Vou te transferir para',
                                         'Favor finalizar como teste. Tenha um ótimo trabalho!']
                      }
    return palavras_chave.copy()


def encontra_chave_step(navegador, cep, numero):
    steps_local = mapeamento_steps(cep, numero)

    while True:
        n_bloco_atual = len(navegador.find_elements(By.XPATH, '//*[@id="messages-list"]/div[1]/div/div/div[2]/div'))
        if n_bloco_atual % 2 == 0 and n_bloco_atual > 0:
            try:
                WebDriverWait(navegador, 1).until(
                    expected_conditions.presence_of_element_located(
                        (By.XPATH, f'//*[@id="messages-list"]/div[1]/div/div/div[2]/div[{n_bloco_atual + 1}]')))
            except:
                break
            else:
                continue
        else:
            sleep(0.5)
    n_ultima_msg = len(navegador.find_elements(
        By.XPATH,f'//*[@id="messages-list"]/div[1]/div/div/div[2]/div[{n_bloco_atual}]/div[2]/div'))
    try:
        for cont in range(1, n_ultima_msg + 1):
            mensagem = str(navegador.find_element(
                By.XPATH,f'//*[@id="messages-list"]/div[1]/div/div/div[2]/div[{n_bloco_atual}]'
                         f'/div[2]/div[{cont}]/div/div/div/div/div[1]/div[1]').text)
            for key, valor in steps_local.items():
                if valor[0].upper() in mensagem.upper():
                    return key
    except:
        return '1'
    else:
        return '1'


def interacao_chat(navegador, CEP, num):
    steps = mapeamento_steps(CEP, num)
    lista_aux_chat = []
    cont = 0
    tempo_erro = 0

    while True:
        chave_step = encontra_chave_step(navegador, CEP, num)
        if chave_step.isnumeric():
            chave_step = int(chave_step)
            tempo_erro += chave_step
        else:
            lista_aux_chat.append(f'{chave_step} - OK')
            tempo_erro = 0

        chave_step = str(chave_step)
        if chave_step in 'Oferta Planos':
            sleep(4)
        elif chave_step in 'Confirma Pedido ,Confirma Pedido2':
            sleep(2)

        try:
            navegador.find_element(By.ID, 'msg-textarea').send_keys(steps[chave_step][1], Keys.ENTER)
        except:
            pass

        if chave_step in 'Transbordo ATH, Consultor Indisponível, Finalização':
            break
        elif chave_step == '1':
            cont += 1
            if cont >= 15:
                chave_step = 'Chave não mapeada'
                lista_aux_chat.append(chave_step)
                break
        else:
            cont = 0
    return lista_aux_chat[:]
