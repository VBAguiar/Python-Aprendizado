from random import choice

aluno01 = str(input('Primeiro aluno: '))
aluno02 = str(input('Segundo aluno: '))
aluno03 = str(input('Terceiro aluno: '))
aluno04 = str(input('Quarto aluno: '))
lista = [aluno01, aluno02, aluno03, aluno04]

print(f'O aluno escolhido foi {choice(lista)}')