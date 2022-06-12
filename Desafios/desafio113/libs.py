def leiaInt(msg):
	while True:
		try:
			num = int(input('{}'.format(msg)))
		except (ValueError, TypeError):
			print('\033[1;31m{}\033[0;0m'.format('ERRO: por favor, digite um número inteiro válido.'))
		except KeyboardInterrupt:
			print('\n\033[1;31m{}\033[0;0m'.format('Usuário preferiu não digitar esse número.'))
			num = 0
			break 
		else:
			break
	return num	

def leiaFlaot(msg):
	while True:
		try:
			num = float(input('{}'.format(msg)))
		except (ValueError, TypeError):
			print('\033[1;31m{}\033[0;0m'.format('ERRO: por favor, digite um número real válido.'))
		except KeyboardInterrupt:
			print('\n\033[1;31m{}\033[0;0m'.format('Usuário preferiu não digitar esse número.'))
			num = 0
			break
		else:
			break
	return num	

