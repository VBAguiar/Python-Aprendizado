from colorama import Style, Fore


def existeArquivo(rota, nome):
	try:
		arquivo = open(f'{rota}/{nome}', 'rt')
		return True
		arquivo.close()
	except FileNotFoundError:
		return False

def criarArquivo(rota, nome):
		arquivo = open(f'{rota}/{nome}', 'wt+')
		arquivo.close() 
	
def lerArquivo(rota, nome):
	try:
		with open(f'{rota}/{nome}', 'rt') as file:
			texto = file.readlines()
			for linha in texto:
				linha = linha.replace('\n', '')
				linha = linha.split(';')
				print(f'{Fore.YELLOW}{linha[0]:<30}{linha[1]} anos{Style.RESET_ALL}')
				
	except FileNotFoundError:
		print(f'{Fore.RED}O arquivo não existie.{Style.RESET_ALL}')

def cadastrarPessoa(nome='desconhecido', idade=0, rota='/', arquivo='cursoemvideo.txt'):
	try:
		with open(f'{rota}/{arquivo}', 'a') as file:
			file.write(f'{nome};{idade}\n')
	except FileNotFoundError:
		print(f'{Fore.RED}Arquivo não encontrado.{Style.RESET_ALL}')
	else:
		print(f'{Fore.GREEN}Novo registro de {nome} adicionado.{Style.RESET_ALL}')

def leiaInt(msg):
	while True:
		try:
			num = int(input('{}{}{}'.format(Fore.GREEN, msg, Style.RESET_ALL)))
		except (ValueError, TypeError):
			print(f'{Fore.RED}ERRO: por favor, digite um número inteiro válido.{Style.RESET_ALL}')
		except KeyboardInterrupt:
			print(f'{Fore.RED}Usuário preferiu não digitar esse número.{Style.RESET_ALL}')
			num = 0
			break 
		else:
			break
	return num	

def leiaString(msg):
	while True:
		try:
			string = str(input('{}{}{}'.format(Fore.GREEN, msg, Style.RESET_ALL)).strip())
		except (ValueError, TypeError):
			print(f'{Fore.RED}ERRO: por favor, digite uma string válida.{Style.RESET_ALL}')
		except KeyboardInterrupt:
			print(f'{Fore.RED}Usuário preferiu não digitar.{Style.RESET_ALL}')
			string = 0
			break 
		else:
			break
	return string
