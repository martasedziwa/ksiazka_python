def print_n(s, n):
	if n > 0:
		print (s)
		print_n(s, n-1)
print_n('marta', 3)		
		
def print_w(s, w):
	while w >0:
		print (s)
		w -= 1
		
print_w('marta', 3)


def petla():
	while True:
		line = input('podaj wyraz')
		if line == 'gotowe':
			break
		print (line)
	print ('Gotowe')

petla()
