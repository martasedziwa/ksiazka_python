plik = open('mwords.txt')
def is_abecedarian():
	ilosc = 0
	for wyraz in plik:
		i = 0
		j = 1
		licznik = 0
		while i < (len(wyraz)-1) and j<len(wyraz):
			if wyraz[i] <= wyraz[j]:
				licznik += 1
				if licznik == len(wyraz)-2:
					print (wyraz)
					ilosc += 1
			else:
				break
		
			i += 1
			j += 1
	print (ilosc)
is_abecedarian()
