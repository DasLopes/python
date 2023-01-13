import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site pudim não está acessivel no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso.')
    print(site.read()) #faz a leitura do site e mostra seu conteúdo
    