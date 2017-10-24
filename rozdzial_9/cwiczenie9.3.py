plik = open('mojplik.txt')
litery = input('podaj zakazane litery:   ')
def avoid(slowo, zak_lit):
	for i in litery:	 
		if i in slowo:
			print ('uzyto zabronionej litery')
			return False
		else:
			pass
	print( 'nie uzyto zadnej zabronionej litery')
	return True
avoid('mart', 'ab')
