def rotation(wyraz,liczba): #obrot
	nowy_wyraz = ''
	for litera in wyraz:
		cyfra_litery = ord(litera)
		if litera.islower():
			cyfra_nowej_litery = cyfra_litery + liczba
			print(cyfra_nowej_litery)
			if cyfra_nowej_litery > 122:
				nowa_litera = chr(96+(cyfra_nowej_litery-122))		
			elif cyfra_nowej_litery < 97:
				nowa_litera = chr(123-(97-cyfra_nowej_litery))	
			else:
				nowa_litera = chr(cyfra_nowej_litery)			
			nowy_wyraz += nowa_litera
						
		else:
			cyfra_nowej_litery = cyfra_litery + liczba
			print(cyfra_nowej_litery)
			if cyfra_nowej_litery > 122:
				nowa_litera = chr(64+(cyfra_nowej_litery-90))
			elif cyfra_nowej_litery < 90:
				nowa_litera = chr(91-(65-cyfra_nowej_litery))	
			else:
				nowa_litera = chr(cyfra_nowej_litery)			
			nowy_wyraz += nowa_litera			
	print(nowy_wyraz)			
		
rotation('melon',-10)
