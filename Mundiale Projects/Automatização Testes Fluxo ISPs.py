from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep

navegador = webdriver.Chrome(r"C:\Users\thiago.bastos\Downloads\chromedriver_win32\chromedriver.exe")

def cidade():
    try:
        navegador.find_element(By.XPATH, '//*[@id="modal-portal"]/div/div/form/div/div/select').click()
        navegador.find_element(By.XPATH, '//*[@id="modal-portal"]/div/div/form/div/div/select/option[2]').click()
        navegador.find_element(By.XPATH, '//*[@id="modal-portal"]/div/div/form/button').click()
    except:
        try:
            navegador.find_element(By.XPATH, '//*[@id="__next"]/section/div/div/main/section/div/select').click()
            navegador.find_element(By.XPATH,
                '//*[@id="__next"]/section/div/div/main/section/div/select/option[2]').click()
        except:
            try:
                navegador.find_element(By.XPATH, '//*[@id="modal-portal"]/div/div/form/div/div/div/select').click()
                navegador.find_element(By.XPATH,
                    '//*[@id="modal-portal"]/div/div/form/div/div/div/select/option[2]').click()
                navegador.find_element(By.XPATH, '//*[@id="modal-portal"]/div/div/form/button').click()
            except:
                pass


def abrir_chat():
    sleep(1)
    navegador.execute_script('document.querySelector("#dots-cta > img").click()')  # clica snippet
    navegador.execute_script('document.querySelector("#dots-chat-cta > img").click()')  # clica no ícone webchat


def esperar_enviar(elemento_procurado, id_html_mensagem, mensagem):
    WebDriverWait(navegador, 20).until(
        expected_conditions.presence_of_element_located((By.XPATH, elemento_procurado)))
    sleep(1)
    navegador.find_element(By.ID, id_html_mensagem).send_keys(mensagem, Keys.ENTER)


def interacao_chat():
    try:
        navegador.switch_to.frame(navegador.find_element(By.ID, 'blip-chat-iframe'))

        esperar_enviar('//*[@id="messages-list"]/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div',
                       'msg-textarea', 'Não')

        esperar_enviar('//*[@id="messages-list"]/div[1]/div/div/div[2]/div[4]/div[2]/div[2]/div/div/div/div/div[1]/div',
                       'msg-textarea', '99010220')

        esperar_enviar('//*[@id="messages-list"]/div[1]/div/div/div[2]/div[6]/div[2]/div[1]/div/div/div/div/div[1]/div',
                       'msg-textarea', '36')

        esperar_enviar('//*[@id="messages-list"]/div[1]/div/div/div[2]/div[8]/div[2]/div[1]/div/div/div/div/div[1]/div[1]',
                       'msg-textarea', 'sim')

        esperar_enviar('//*[@id="messages-list"]/div[1]/div/div/div[2]/div[10]/div[2]/div[1]/div/div/div/div/div[1]/div',
                       'msg-textarea', 'Favor encerrar como teste. Tenha um ótimo trabalho! :)')
        return "OK"
    except Exception as erro:
        return f"Não OK, erro {erro.__class__}"


# LISTA com LPs
sites = [['https://ofertasblinktelecom.com.br/',
          'https://ofertasbrisanet.com.br',
          'https://ofertastely.com.br/',
          'https://ofertasligue.net/',
          'https://ofertassumicity.com.br/',
          'https://ofertasvipbrtelecom.com.br/'],

         ['https://ofertastvn.com.br',
          'http://ofertascoprel.com.br/',
          'https://ofertasnova.com.br',
          'https://ofertasdesktop.com.br',
          'https://ofertassoumaster.com.br/',
          'https://ofertasazza.net.br/',
          'https://ofertasfleetnet.com.br/'],

         ['https://ofertasvalenet.com.br/',
          'http://ofertasmobtelecom.com.br/',
          'http://ofertasweclix.com.br',
          'https://ofertascabonnet.com.br/',
          'http://ofertasercomtel.com.br/']]

while True:
    print('''Realizar testes para qual Squad?
0 - Todos os Squads das ISPs
1 - EVA
2 - WALL-e
3 - BURN-e''')
    resp = int(input('Opção: '))
    if resp in range (0, 4):
        break
    print('\033[1:31mOpção inválida!\033[m')

if resp == 0:
    for i, squad in enumerate(sites):
        for lp in squad:
            if sites[i].index(lp) == 0:
                navegador.get(lp)
            else:
                navegador.switch_to.new_window('tab')
                navegador.get(lp)
            cidade()
            abrir_chat()
            print(interacao_chat())

else:
    resp -= 1
    for lp in sites[resp]:
        if sites[resp].index(lp) == 0:
            navegador.get(lp)
        else:
            navegador.switch_to.new_window('tab')
            navegador.get(lp)
        cidade()
        abrir_chat()
        print(interacao_chat())
