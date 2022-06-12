try:
	a = int(input())
	b = int(input())
	r = a / b
except ZeroDivisionError:
	print('ERRO!!!')
else:
	print(f'{r}')
finally:
	print('volte sempre')
