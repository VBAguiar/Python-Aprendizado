def notas(*notas, sit=False):
	"""
	notas(*n, sit=False)
		-> Função para analisar nota e situações de vários alunos.
	
	"""
	total = len(notas); maior = max(notas); menor = min(notas); media = sum(notas) / 2
	resp = {'total': total, 'maior': maior, 'menor': menor, 'media': media}
	situcao = None
	
	if sit == True:
		if media >= 7:
			resp['situação'] = 'BOA'
		elif media >= 5:
			resp['situação'] = 'RAZOAVEL'
		else:
			resp['situação'] = 'RUIM'
	return resp
	

if __name__ == "__main__":
	resp = notas(2.0, 5.60, 4.5, 8.0, sit=True)
	print(resp)

