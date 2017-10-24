def eval_loop():
	while True:
		x = input('podaj wartosc:  ')
		y = eval(x)
		print (y)
		print (type(y))
		if x == 'gotowe':
			break
		z = y
	print (z)

eval_loop()
