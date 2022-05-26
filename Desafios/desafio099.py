from random import randint
from time import sleep

def maior(*arg):
	arg = list(arg)
	if len(arg) == 0:
		arg.append(0)
	
	print('-=' * 30)
	print(f'Analisando valores passados...')
	for c in arg:
		print(c, flush=True, end=' ')
		sleep(0.07)
	print(f'Foram informados {len(arg)} valores ao todo.')
		
	maior = arg[0] 
	for c in arg:
		if c >= maior:
			maior = c
	print(f'O maior valor informado foi {maior}')

if __name__ == "__main__":
	maior(2, 9, 4, 5, 7, 1)
	maior(4, 7, 0)
	maior(1, 2)
	maior(6)
	maior()
