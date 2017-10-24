def wypisz():
	print("marta")


def do_n(obiekt_funkcji, n):
	if n <= 0:
		return
	else:
		obiekt_funkcji()    
		do_n(obiekt_funkcji, n-1)
		
do_n(wypisz,3)


def recurse(n, s):
	if n == 0 :
		print (s)
	else: 
		recurse (n-1, s + n)
recurse(-1, 0)
