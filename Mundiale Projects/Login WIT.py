from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

def login_wit(browser, usuario, senha):
    """
    Função responsável por realizar o login no WIT
    :param browser: Instância do browser [firefox, chrome, ...]
    :param usuario: Usuário para login
    :param senha: Senha do usuário informado
    """
    browser.get(r'http://wit/#!/app/feed')
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="login"]').send_keys(usuario, Keys.TAB, senha, Keys.ENTER)

navegador = Chrome()
usuario = str(input('Favor digitar o usuário: '))
senha = str(input('Agora a senha: '))

login_wit(navegador, usuario, senha)
# '1002062870620' 'Ts@1thigotsb'