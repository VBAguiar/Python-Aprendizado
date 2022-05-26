def dobra(valores):
	pos = 0 
	while pos < len(valores):
		valores[pos] *= 2
		pos += 1

valores = [2, 4, 5, 7, 1, 4, 9]
dobra(valores)
print(valores)
