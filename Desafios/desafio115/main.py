from menu import menu, titulo
from colorama import Style, Fore
from menu.uteis import lerArquivo, criarArquivo, existeArquivo, cadastrarPessoa, leiaInt, leiaString

pasta, arquivo = '/home/barbosa/Documentos/Projects/Python-Aprendizado/Desafios/desafio115', 'cursoemvideo.txt'

if __name__ == "__main__":
	if existeArquivo(pasta, arquivo):
		pass
	else:
		criarArquivo(pasta, arquivo)
		print('Criado arquivo cursoemvideo.txt')
	while True:
		menu('Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema')
		try:
			resp = int(input('{}{}{}'.format(Fore.GREEN, 'Sua Opção: ', Style.RESET_ALL)))
				
			if resp == 1:
				titulo('Opção 1'.upper())
				titulo('Pessoas Cadastradas') 
				lerArquivo(pasta, arquivo)
					
			elif resp == 2:
				titulo('Opção 2'.upper())
				titulo('Novo Cadastro')
				nome = leiaString('Nome: ')
				idade = leiaInt('Idade: ')
				cadastrarPessoa(nome, idade, pasta, arquivo)
					
			elif resp == 3:
				titulo('Saindo do sistema.. Até logo!!'.upper())
				break
					
			else:
				print(f'{Fore.RED}ERRO! Digite uma opção válida!{Style.RESET_ALL}')
				
		except Exception:
			print(f'{Fore.RED}ERRO: por favor, digite um número inteiro válido.{Style.RESET_ALL}')
	
