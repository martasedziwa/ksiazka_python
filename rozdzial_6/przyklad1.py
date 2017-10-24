def is_between (x, y, z):
	if (x <= y <= z ):
		return True
	return False
is_between(1,4,3)

import math
def distance(xc,yc,xp,yp):
	dx = xp - xc
	dy = yp - yc
	dsquared = dx ** 2 + dy ** 2 
	result = math.sqrt(dsquared)
	return result
	
distance(1,2,4,6)


def factorial(n):
	if not isinstance(n, int):
		print('wartosc n nie jest liczba calkowita')
		return False
	elif n < 0 :
		print ('wartosc n jest ujemna')
		return False
	elif n == 0 :
		return 1
	else:
		x = factorial(n-1)
		wynik = n *  int (x)
		return (wynik)

factorial (-6)

print ('-------')


def fibonacci(n):
	if not isinstance(n, int):
		print('wartosc n nie jest liczba calkowita')
		return False
	elif n < 0 :
		print ('wartość n jest ujemna')
		return False
	else:  
		if n == 0 :
			return 0
		elif n == 1:
			return 1
		else:
			wynik = fibonacci (n-1) + fibonacci (n-2)
			return (wynik)
	
	
fibonacci (5)


print ('------------')

x = isinstance (3, str)
print (x)

print ('--------')

