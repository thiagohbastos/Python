import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from funcoes_novoBOT import tratar_cidade, abrir_snippet, url_lps, encontra_chave_step, mapeamento_steps, interacao_chat

navegador = webdriver.Chrome()
sites = url_lps()
steps = mapeamento_steps(sites['WALL-E']['AZZA'][1], sites['WALL-E']['AZZA'][2])
resultado_etapas = []

try:
    navegador.get('https://ofertasazza.net.br/')
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

lista_auxiliar = interacao_chat(navegador, sites['WALL-E']['AZZA'][1], sites['WALL-E']['AZZA'][2])
for cont in range(0, len(lista_auxiliar)):
    resultado_etapas.append(lista_auxiliar[cont])

print(resultado_etapas)
