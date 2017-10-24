def podaj_wymiary ():
	a = int(input('podaj dlugosc boku a:  '))
	b = int(input('podaj dlugosc boku b:  '))
	c = int(input('podaj dlugosc boku c:  '))
	is_triangle (a, b, c)


def is_triangle (a, b, c):
	if a >= b + c or  b >= a + c or c >= a + b:
		print ('NIE')
	else:
		print ('TAK')

podaj_wymiary()
