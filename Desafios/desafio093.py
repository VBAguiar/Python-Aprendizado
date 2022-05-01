jogador = {'nome': str(input('Nome do jogador: '))}
gols = []

conp = int(input('Quantos partidas {} jogou?: '.format(jogador['nome'])))
for c in range(0, conp):
	gols.append(int(input('Quantos gols na partida {}: '.format(c))))

jogador['gols'] = gols[:]
jogador['total'] = sum(gols)

print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
	print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f"O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas")

for i in range(0, len(jogador['gols'])):
	print(f"	=> Na partida {i}, fez {jogador['gols'][i]}")

print(f"Foi um total de {jogador['total']}.")
