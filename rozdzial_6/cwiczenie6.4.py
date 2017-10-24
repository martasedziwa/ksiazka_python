def is_power(a, b):
	if a == b :
		print (a, 'jest pierwsza potega liczby', b)
	elif a == 1: 
		print ('potega liczby', b, 'jest 0')
	x = a
	wynik = a
	licznik = 1
	while wynik > b:
		licznik += 1
		a = wynik
		wynik = a//b
		print('licznik', licznik)
		if wynik == b:
			print (x,'to', licznik, 'potega', b)


is_power(125,5)
