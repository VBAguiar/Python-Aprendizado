def moeda(valor):
	valor = f'R${valor:.2f}'.replace('.', ',')
	return valor

def resumo(valor, am, rd):
	print('-'*45)
	print('		RESUMO DO VALOR		')
	print('-'*45)
	
	print(f'Preco analisado: 	R${moeda(valor)}')
	print(f'Dobro de preco:		R${dobro(valor, True)}')
	print(f'Metade do preco:	R${metade(valor, True)}')
	print(f'{am}% de aumento:		R${aumentar(valor, am, True)}')
	print(f'{rd}% de reducao:		R${diminuir(valor, rd, True)}')
	print('-'*45)

def metade(valor, form=False):
	if form == True:
		return moeda(valor / 2)
	return valor / 2

def dobro(valor, form=False):
	if form == True:
		return moeda(valor * 2)
	return valor * 2

def aumentar(valor, taxa, form=False):
	if form == True:
		return moeda(valor + (valor * taxa/100))
	return valor + (valor * taxa/100)

def diminuir(valor, taxa, form=False):
	if form == True:
		return moeda(valor - (valor * (taxa/100)))
	return valor - (valor * (taxa/100))
