def podaj_wartosci ():
	a = int(input('podaj wartosc a:  '))
	b = int(input('podaj wartosc b:  '))
	c = int(input('podaj wartosc c:  '))
	n = int(input('podaj wartosc n:  '))
	check_fermat(a,b,c,n)
	
	
def check_fermat(a,b,c,n):
	if n > 2 and (a**n + b**n == c**n):
		print('Do licha, Fermat sie mylil')
	else:
		print('Nie to nie dziala')

podaj_wartosci()
		
