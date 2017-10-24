plik = open('mojplik.txt')
def uses_all(litery):  
	for slowo in plik:
		licznik = 0
		while True:
			for i in litery:		
				if i not in slowo:
					break
				else:
					licznik += 1
					if licznik >= len(litery):
						print (slowo)
			break
uses_all('ly')
