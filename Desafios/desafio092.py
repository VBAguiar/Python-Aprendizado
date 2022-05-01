from datetime import date

nome = str(input('Nome: '))
anonacs = int(input('Ano de Nascimento: '))
carteira = int(input('Carteira de Trabalho (0 não tem): '))

ano = date.today()
idade = int(ano.year) - anonacs
dados = {'nome': nome, 'idade': idade, 'ctps': carteira}

if carteira == 0:
	for k, v in dados.items():
		print(f'	- {k} tem o valor {v}')
else:
	anocon = int(input('Ano de Contrataçao: '))
	sal = int(input('Salário: '))
	aps = idade + ((anocon + 35) - int(ano.year))
	dados['contratação'] = anocon; dados['salário'] = sal; dados['aposentadoria'] = aps
	
	for k, v in dados.items():
		print(f'	- {k} tem o valor {v}')
	
