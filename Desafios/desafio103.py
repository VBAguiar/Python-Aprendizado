def ficha(nome, gols):
	nome = nome
	gols = gols
	if len(nome) == 0:
		nome = '<desconhecido>'
	
	if len(gols) == 0:
		gols = '0'
	elif gols.isnumeric() == False:
		gols = '0'
		
	
	return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


if __name__ == "__main__":
	nome = str(input('Nome do Jogador: '))
	gols = str(input('Número de Gols: '))
	print(ficha(nome, gols))
