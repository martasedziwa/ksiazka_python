def dzielnik(a, b):
	x = 1
	if a == 0:
		print (b)
		return (b)
	elif b == 0: 
		print (a)
		return (a)
	
	while x <= a or x <= b: # or x <= c:
		if a % x == 0 and b % x == 0:  #and c % x == 0:
			nwd = x
			x += 1 
		else: 
			x += 1	
		
	print(nwd)
	return (nwd)
	
dzielnik(1545675, 0)
