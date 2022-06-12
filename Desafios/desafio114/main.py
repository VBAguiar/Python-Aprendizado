import urllib
import urllib.request

try:
	site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.request.URLError:
	print('\033[1;31m{}\033[0;0m'.format('O site Pudim não está acessível não momento.'))
else:
	print('Consegui acessar o site Pudim com sucesso.')
