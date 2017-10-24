plik = open('mojplik.txt')
def zagadka():
	for wyraz in plik:
		i = 0
		j = 1
		suma = 0
		while i < len(wyraz) and j < len(wyraz)-1:
			litera1 = wyraz[i] 
			litera2 = wyraz[j]
			if litera1 == litera2:
				suma += 1
				i += 2
				j += 2
				if suma == 3:
					print('w wyrazie', wyraz, 'sa 3 powtorzenia')# poprawićć
					print('---------')
				elif suma > 3:
					print('w wyrazie', wyraz, 'jest wiecej niz 3 powtorzenia')
					print('wyraz sie nie nadaje')
					print('---------')
					break
			elif litera1 != litera2 and suma == 1:
				break
			elif litera1 != litera2 and suma == 2:
				break
			else:
				i += 1
				j += 1
zagadka()
			
