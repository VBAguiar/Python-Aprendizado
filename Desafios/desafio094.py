pessoas = []

while True:
	nome = str(input('Nome: '))
	sexo = ' '
	
	while sexo not in 'MF':
		sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
	
	idade = 'bk'
	
	while idade.isnumeric() != True:
		idade = str(input('Idade: '))
	
	pessoa = {'nome': nome, 'sexo': sexo, 'idade': int(idade)}; pessoas.append(pessoa)
	continuar = ' '
	
	while continuar not in 'SN':
		continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
	
	if continuar == 'N':
		break

print('-=' * 30)

print(f'A) Ao todo temos {len(pessoas)} pessoas cardastradas.')
somaIdade = 0
for ps in pessoas:
	somaIdade += ps['idade']

print(f'B) A média de Idade é de {somaIdade/2}.')
print(f'C) As mulheres cadastradas foram ', end='')
for ps in pessoas:
	if ps['sexo'] == 'F':
		print(ps['nome'], end=' ')
print(f'\nD) Lista da pessoas que estão acima da média: ')
for ps in pessoas:
	if ps['idade'] > somaIdade/2:
		print(f"nome = {ps['nome']}; sexo = {ps['sexo']}; idade = {ps['idade']}")



