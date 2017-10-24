def dzielnik(a, b,c):
	x = 1
	while x <= a or x <= b or x <= c:
		if a % x == 0 and b % x == 0 and c % x == 0:
			nwd = x
			x += 1 
		else: 
			x += 1	
		
	print(nwd)
	
	
dzielnik(1545675, 1892745, 7896545)

