def escreva(texto):
	print('~' * (len(texto) + 2))
	print(' {}'.format(texto))
	print('~' * (len(texto) + 2))

if __name__ == "__main__":
	escreva('Gustavo Guanabara')
	escreva('Curso de Python no Youtube')
	escreva('CeV')
