def first(world):
	return world[0]
	
def last(world):
	return world[-1]
	
def middle(world):
	return world[1]
	
	
def is_palindrome(slowo):
	n = len(slowo)
	licznik = 0
	for i in range(0, n):
		if slowo[i] == slowo[n-(i+1)]:
			licznik += 1
			if licznik == n:
				return True
		else:
			return False
		
is_palindrome('ad')
