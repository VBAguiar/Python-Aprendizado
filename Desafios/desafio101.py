from datetime import datetime

def voto(ano):
	print(f'Com {ano} anos:', end=' ')
	
	if ano >= 90 or ano <= 16:
		return 'OPCIONAL.'
	elif ano >= 18:
		return 'OBRIGATÓRIO.'
	else:
		return 'NÃO VOTA:'
		
if __name__ == "__main__":
	ano = int(input('Em que ano você nasceu? '))
	data_atual = datetime.today()
	print(voto(data_atual.year - ano))
	
