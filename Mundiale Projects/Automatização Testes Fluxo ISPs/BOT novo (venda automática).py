import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import time, sleep
from funcoes_novoBOT import tratar_cidade, abrir_snippet, url_lps, encontra_chave_step, mapeamento_steps

navegador = webdriver.Chrome()
sites = url_lps()
steps = mapeamento_steps(sites['EVA']['VIP'][1], sites['EVA']['VIP'][2])
resultado_etapas = list()
resultado_geral = {'VIP': ''}
indices = ['Carregamento LP', 'Seleciona Cidade', 'SNIPPET', 'CHAT']

try:
    navegador.get(r'https://ofertasvipbrtelecom.com.br/')
except:
    resultado_etapas.append('Fora do Ar')
else:
    resultado_etapas.append('OK')

resultado_etapas.append(tratar_cidade(navegador))
resultado_etapas.append(abrir_snippet(navegador))

try:
    navegador.switch_to.frame(navegador.find_element(By.ID, 'blip-chat-iframe'))
    WebDriverWait(navegador, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="messages-list"]/div[1]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div[1]/div')))
except:
    resultado_etapas.append('Não carregou')
else:
    resultado_etapas.append('OK')

cont = 0
tempo_erro = 0
while True:
    chave_step = encontra_chave_step(navegador, sites['EVA']['VIP'][1], sites['EVA']['VIP'][2])
    print(chave_step)

    if chave_step.isnumeric():
        chave_step = int(chave_step)
        tempo_erro += chave_step
    else:
        if tempo_erro > 0:
            indices.append(tempo_erro)
        indices.append(chave_step)
        tempo_erro = 0
    chave_step = str(chave_step)
    if chave_step == 'Oferta Planos':
        sleep(4)
    try:
        navegador.find_element(By.ID, 'msg-textarea').send_keys(steps[chave_step][1], Keys.ENTER)
    except:
        pass
    if chave_step in 'Transbordo ATH, Consultor Indisponível, Finalização':
        break
    elif chave_step == 1:
        cont += 1
        if cont >= 15:
            break
    else:
        cont = 0
print(indices)
