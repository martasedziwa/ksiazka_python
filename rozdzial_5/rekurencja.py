def dzialanie(a, b):
	print(a*b)

def dodawanie(c, d):
	print(c + d)
	
def wypisz():
	print('marta')
	
def rek ( obiekt_funkcji1, obiekt_funkcji2, n, a, b,c, d):
	if n <= 0:
		return
	else:
		wypisz()
		obiekt_funkcji1(a, b)
		obiekt_funkcji2(c, d)
		rek(obiekt_funkcji1, obiekt_funkcji2, n-1, a, b,c ,d)
	
rek(dzialanie, dodawanie, 3, 2, 2, 1, 1)
