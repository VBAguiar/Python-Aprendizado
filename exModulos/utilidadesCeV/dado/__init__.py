def leiaDinheiro(msg):
	while True:
		valor = input('{}'.format(msg))
		if valor.isnumeric() == False:
			print('ERRO:\033[1;31m "{}" {}\033[0;0m'.format(valor, 'Valor invalido'))
		else:
			break
	valor = valor.replace(',', '.')
	return float(valor)
