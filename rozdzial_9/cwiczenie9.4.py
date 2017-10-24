plik = open('mojplik.txt')
def uses_only(litery):
	for slowo in plik:
		licznik = 0
		while True:
			for i in slowo:		
				if i not in litery:
					break
				else:
					licznik += 1
					if licznik == len (slowo) -1:
						print (slowo)
			break

