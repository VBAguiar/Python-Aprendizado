def leiaInt(n):
	resp = None
	if n.isnumeric() == True:
		resp = n
	else:
		while True:
			resp = str(input('Digite um numero: ')) 
			
			if resp.isnumeric() == True:
				break
			else:
				print('ERRO!!! Digite um número inteiro válido.') 
	return resp


if __name__ == "__main__":
	n = leiaInt('Digite um número')
	print(f'Você acabou de digita o número {n}')
