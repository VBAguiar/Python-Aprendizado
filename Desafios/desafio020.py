from random import shuffle

aluno01 = str(input('Primeiro aluno: '))
aluno02 = str(input('Segundo aluno: '))
aluno03 = str(input('Terceiro aluno: '))
aluno04 = str(input('Quarto aluno: '))

alunos = [aluno01, aluno02, aluno03, aluno04]
shuffle(alunos)
print(alunos)