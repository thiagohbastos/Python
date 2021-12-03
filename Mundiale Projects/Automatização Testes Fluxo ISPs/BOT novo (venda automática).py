import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import time, sleep
from funcoes_novoBOT import tratar_cidade, abrir_snippet, url_lps, encontra_chave_step, mapeamento_steps

navegador = webdriver.Chrome()
sites = url_lps()
steps = mapeamento_steps(sites['EVA']['BRISANET'][1], sites['EVA']['BRISANET'][2])

#ignorável por enquanto
resultado_geral = dict()
#Fim ignorável

resultado_etapas = []

try:
    navegador.get(r'https://ofertasbrisanet.com.br/')
except:
    resultado_etapas.append('LP Fora do Ar')
else:
    resultado_etapas.append('LP OK')

resultado_etapas.append(tratar_cidade(navegador))
resultado_etapas.append(abrir_snippet(navegador))

try:
    navegador.switch_to.frame(navegador.find_element(By.ID, 'blip-chat-iframe'))
except:
    resultado_etapas.append('CHAT não OK.')
else:
    resultado_etapas.append('CHAT OK')

cont = 0
tempo_erro = 0

while True:
    chave_step = encontra_chave_step(navegador, sites['EVA']['BRISANET'][1], sites['EVA']['BRISANET'][2])
    #print(chave_step)

    if chave_step.isnumeric():
        chave_step = int(chave_step)
        tempo_erro += chave_step
    else:
        if tempo_erro > 0:
            resultado_etapas.append(tempo_erro)
        resultado_etapas.append(chave_step)
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
print(resultado_etapas)
