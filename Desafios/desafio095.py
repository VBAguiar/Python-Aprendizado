from tabulate import tabulate

listaDeJogadores = []
tabulateListe = []
cod = 0

while True:
	gols = []
	nome = str(input('Nome do jogador: '))
	qpartidas = int(input('Quantas partidas {} jogou? '.format(nome)))
	
	for c in range(1, qpartidas+1):
		gol = int(input(     'Quantos gols na partida {} '.format(c)))
		gols.append(gol)
	
	jogador = {'cod': cod, 'nome': nome, 'gols': gols, 'total': sum(gols)}; listaDeJogadores.append(jogador.copy())
	
	continuar = ' '
	cod += 1
	while True:
		continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
	
		if continuar in 'SN':
			break
		
		print('Digite novamente')
	
	if continuar == "N":
		break 

print('-='*50)	
print(tabulate(listaDeJogadores, headers='keys'))
print('-'*32)

jogador = 0
while jogador != 999:
	jogador = int(input('Mostra dados de qual jogador? (999 para parar) '))
	
	if jogador == 999:
		break
	
	if jogador >= len(listaDeJogadores):
			print(f'ERRO!! Não existe jogador com código {jogador}!')
			jogador = int(input('Mostra dados de qual jogador? (999 para parar) '))
	
	for i in range(0, len(listaDeJogadores)):
		if i == jogador:
			for c, i in enumerate(listaDeJogadores[i]['gols']):
				print(f'No jogo {c} fez {i}.')

print('!!VOLTE SEMPRE!!')
