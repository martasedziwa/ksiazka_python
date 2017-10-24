def odwrocony_wiek():
	licznik = 0
	i = str(2)
	j = str(20)
	while int(j) < 100:
		i = str(i)
		j = str(j)
		if i.zfill(2) == j[::-1]:
			j = int(j) 
			i = int(i) 
			licznik += 1
			
			if licznik == 6 :
				print ('mam', j, 'lat')
			j += 1
			i += 1
		else:
			j = int(j) 
			i = int(i) 
			j += 1
			i += 1
odwrocony_wiek()
