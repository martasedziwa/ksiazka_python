		
import math
def mysqrt(x,a):
	while True:
		y = (x + a/x)/2
		if y == x :
			break
		x = y
	return (x)

def test_square_root(x,a):
	print('a', ' ' , 'mysqrt(a)', ' ' , 'math.sqrt(a)', ' ' , 'diff')
	print('-'*70)
	for a in range (1, 10):
		print(a,' ' , mysqrt(x,a), ' ' , math.sqrt(a), ' ' , math.sqrt(a)- mysqrt(x,a))
test_square_root(7,25)
