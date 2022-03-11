import pandas as pd
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

navegador = Chrome()
navegador.maximize_window()


# Fazer login
navegador.get('https://mundiale.blip.ai/application')
email = input('Favor informar o e-mail do usuário Blip: ')
senha = input('Agora informe a senha: ')
navegador.find_element_by_css_selector(
    '#email').send_keys(email, Keys.TAB)
navegador.find_element_by_css_selector(
    '#password').send_keys(senha, Keys.ENTER)

#Coletando nome dos BOTs do BLIP
sleep(2)
list_blip_bots = []
num_bots = len(navegador.find_elements(
    By.XPATH, '/html/body/div[3]/div[1]/section/ui-view/div/div/div/contact-list/contact'))
for x in range(1, num_bots + 1):
    list_blip_bots.append(navegador.find_element(
        By.XPATH, f'/html/body/div[3]/div[1]/section/ui-view/div/div/div/contact-list/contact[{x}]/div/ng-include/a/div/div/div[2]/span').text)


#Coletando nome dos BOTs de arquivo EXCEL (Banco de dados)
list_banco_bots = pd.read_excel('Conferência BOTs BLIP.xlsx')
list_banco_bots = pd.DataFrame.to_dict(list_banco_bots)
list_banco_bots = list_banco_bots['bot_name']


#Resultado 1
result_blip_in_banco = []
for v in list_blip_bots:
    if v in list_banco_bots.values():
        result_blip_in_banco.append([v, 1])
    else:
        result_blip_in_banco.append([v, 0])
result_blip_in_banco = pd.DataFrame(data=result_blip_in_banco, columns=[
                                    'Nome do BOT no Blip', 'Está no BANCO'])

#Resultado 2
result_banco_in_blip = []
for k, v in list_banco_bots.items():
    if v in list_blip_bots:
        result_banco_in_blip.append([v, 1])
    else:
        result_banco_in_blip.append([v, 0])
result_banco_in_blip = pd.DataFrame(data=result_banco_in_blip, columns=[
                                    'Nome do BOT no Banco', 'Está no BLIP'])

#Salvando resultado
arquivo = pd.ExcelWriter(
    'Resultado Conferência BOTs BLIP.xlsx', engine='xlsxwriter')
result_blip_in_banco.to_excel(arquivo, index=False, sheet_name='Conf_BLIP')
result_banco_in_blip.to_excel(arquivo, index=False, sheet_name='Conf_BANCO')
arquivo.save()
arquivo.close()
navegador.quit()