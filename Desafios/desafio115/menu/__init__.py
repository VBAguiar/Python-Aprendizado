from colorama import Fore, Style

def titulo(msg):
	print('-'*42)
	print(f'{Fore.CYAN}{msg}{Style.RESET_ALL}'.center(42))
	print('-'*42)
	
def menu(*op):
	titulo(f'MENU PRINCIPAL')
		
	print(f'{Fore.YELLOW}1{Style.RESET_ALL} - {Fore.BLUE}{op[0]}{Style.RESET_ALL}')
	print(f'{Fore.YELLOW}2{Style.RESET_ALL} - {Fore.BLUE}{op[1]}{Style.RESET_ALL}')
	print(f'{Fore.YELLOW}3{Style.RESET_ALL} - {Fore.BLUE}{op[2]}{Style.RESET_ALL}')
	print('-'*42)
