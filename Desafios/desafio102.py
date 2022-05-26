def fatorial(num, show=False):
	"""
	-> Calcula o Fatorial de um número.
	:param n: O número a ser calculado.
	:param show: (opcional) Mostrar ou não a conta.
	:raturn: O valor fatorial de um número n.  
	"""
	temp = num
	cont = 0
	while True:
		temp -= 1
		if temp <= 0:
			break
		 
		if show == True:
			if cont == 0:
				print(num, end='') 
			print(f' x {temp}', end='')
		num *= temp
		cont += 1
	print(f'\n{num}')
if __name__ == "__main__":
	fatorial(5, show=True)
