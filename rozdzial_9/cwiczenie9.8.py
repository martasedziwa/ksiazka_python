def palindrom_mil():
	for liczba in range(100000, 1000000):
		x = str(liczba)
		liczba_poczatkowa = x		
		if x[2] == x[5] and x[3] == x[4]:
			x = int(x)
			x += 1
			x = str(x)
			if x[1] == x[5] and x[2] == x[4]:
				x = int(x)
				x += 1
				x = str(x)
				if x[1] == x[4] and x[2] == x[3]:
					print(liczba_poczatkowa)
palindrom_mil()
