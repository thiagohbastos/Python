import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print(f'\033[1:33mERRO! O site Pudim não está acessível no momento. \033[m')
else:
    print('\033[1:32mConsegui acessar o site Pudim com sucesso!\033[m')
    print(site.read())