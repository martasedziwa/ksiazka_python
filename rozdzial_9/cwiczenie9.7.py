plik = open('mojplik.txt')
def powtorzenia():
	for wyraz in plik:
		print (wyraz)
		roznice = 0
		licznik = 0 
		i = 0
		j = 1
		while j <len(wyraz)-1:
			if wyraz[i] == wyraz[j]:
				licznik += 1
				i += 2
				j += 2
				if licznik == 3:
					print ('ok')
				if licznik > 3:
					print ('wyraz jednak sie nie nadaje')
			elif wyraz[i] != wyraz[j]:
				roznice += 1
				if licznik == 2:
					print ('wyraz ma 2 powtorzenia')
				elif licznik == 1:
					print ('wyraz ma 1 powtorzenia')
				if licznik == 3 
				i += 1
				j += 1
				if roznice == len(wyraz)-2:
					print ('wyraz sie nie nadaje')
	
		
	
powtorzenia()
