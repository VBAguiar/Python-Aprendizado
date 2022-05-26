from time import sleep

def contar(i, f, p):
	print(f'Contagem de {i} até {f} de {p} em {p}')
	if p < 0:
		p *= -1
	
	if p == 0:
		p = 1
	
	if i > f:
		for c in range(-i, -f+1, p): 
			print(f'{c * -1} ', flush=True, end='')
			sleep(0.07)

	
	for c in range(i, f+1, p):
		print(f'{c} ', flush=True, end='')
		sleep(0.07)
	
	print('FIM!')
	
if __name__ == "__main__":
	print('-=' * 30)
	contar(1, 10, 1)
	print('-=' * 30)
	contar(10, 0, 2)
	print('-=' * 30)
	print('Agora é sua vez de pensonalizar a contagem!')
	
	i = int(input('Início: '))
	f = int(input('Fim: '))
	p = int(input('Passo: '))
	
	contar(i, f, p)
