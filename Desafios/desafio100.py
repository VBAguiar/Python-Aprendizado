from random import randint
from time import sleep

def sorteia(lista):
	print('Sorteando 5 valores de uma lista: ', end=' ')
	
	for c in range(0, 5):
		r = randint(1, 10)
		print(f'{r}', flush=True, end=' ')
		sleep(0.30)
		lista.append(r) 
	
	print('PRONTO!!')

def somaPar(lista):
	soma = 0
	for c in lista:
		if c % 2 == 0:
			soma += c
	print(f'Somando os valores pares de {lista}, temos {soma}')
	
if __name__ == "__main__":
	lista = []
	sorteia(lista)
	somaPar(lista)
