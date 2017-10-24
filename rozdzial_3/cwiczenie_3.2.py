def do_twice(obiekt_funkcji, wartosc):
	obiekt_funkcji(wartosc)
	obiekt_funkcji(wartosc)
	
def print_spam(wartosc):
	print('wartosc')

def print_twice(wyraz):
	print(wyraz)
	print(wyraz)

def do_four(obiekt_funkcji, wartosc):
	do_twice(obiekt_funkcji, wartosc)
	do_twice(obiekt_funkcji, wartosc)
	
	
do_four(print_twice, 'spam')
	


