def area(l, c):
	return l * c

if __name__ == "__main__":
	l = float(input('LARGURA (m): '))
	c = float(input('COMPRIMENTO (m): '))
	a = area(l, c)
	print(f'A área de um terreno {l:.1f}x{c:.1f} é de {a}m²')
	
