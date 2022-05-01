listaDeJogadores = []

while True:
	gols = []
	nome = str(input('Nome do jogador: '))
	qpartidas = int(input('Quantas partidas {} jogou? '.format(nome)))
	
	for c in range(1, qpartidas+1):
		gol = int(input(     'Quantos gols na partida {} '.format(c)))
		gols.append(gol)
	jogador = {'nome': nome, 'gols': gols, 'total': sum(gols)}; listaDeJogadores.append(jogador)

print('cod ', end=' ')
for i in jogadores.keys():
	print(f'{i:>4}')

print('-'*30)




