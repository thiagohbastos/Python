from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from openpyxl import Workbook, load_workbook

navegador = webdriver.Chrome("chromedriver")
navegador.get(r"https://ads.google.com/aw/billing/billingsetups?ocid=558852957&euid=552022965&__u=9001822285&uscid=558852957&__c=1452045493&authuser=1&subid=ww-ww-et-g-aw-a-vasquette_ads_cons_1%21o2m--ahpm-0000000080-0000000001")

navegador.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys('thiago.bastos@mundiale.com.br')
navegador.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()

#Atualizando a aba 'Geral'
tabela = load_workbook(r"C:\Users\thiago.bastos\Desktop\GERAL\Relatório Saldo Atualizado.xlsx")
aba_ativa = tabela.active
for linha in range(3, len(aba_ativa['D']) + 1):
    if aba_ativa[f'D{linha}'].value >= 0:
        aba_ativa[f'C{linha}'] = aba_ativa[f'D{linha}'].value

tabela.save(r"C:\Users\thiago.bastos\Desktop\GERAL\Teste.xlsx")