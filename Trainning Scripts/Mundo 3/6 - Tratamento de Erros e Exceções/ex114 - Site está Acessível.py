from selenium.webdriver import Chrome

driver = Chrome()

try:
    driver.get("http://pudim.com.br/")
except Exception as erro:
    print(f'\033[1:33mERRO {erro.__class__}. O site Pudim não está acessível no momento. \033[m')
else:
    print('\033[1:32mConsegui acessar o site Pudim com sucesso!\033[m')
finally:
    driver.quit()
