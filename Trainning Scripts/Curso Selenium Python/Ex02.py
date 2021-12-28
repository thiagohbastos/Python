from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

navegador = Chrome()
navegador.get("https://curso-python-selenium.netlify.app/exercicio_02.html")
sleep(1)

n_esperado = int(navegador.find_elements(By.TAG_NAME, 'p')[1].text[-1])

while True:
    navegador.find_element(By.TAG_NAME, "a").click()
    resultado = int(navegador.find_elements(By.TAG_NAME, 'p')[-1].text[-1])
    if n_esperado == resultado:
        break
sleep(1)
print(f'Você ganhou após {len(navegador.find_elements(By.TAG_NAME, "p")) - 2} tentativas.')
navegador.quit()
