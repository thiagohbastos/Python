from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

ex01 = dict()
navegador = Chrome()

navegador.get("https://curso-python-selenium.netlify.app/exercicio_01.html")
sleep(1)

h1 = navegador.find_element(By.TAG_NAME, 'h1').text
ex01[h1] = dict()

all_p = navegador.find_elements(By.TAG_NAME, 'p')

for atributo in range(0, len(all_p)):
    ex01[h1][f'texto{atributo + 1}'] = all_p[atributo].text

print(ex01)