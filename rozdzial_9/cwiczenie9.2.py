plik = open('words.txt')
procent = 0
calosc = 0
for wyraz in plik:
	calosc += 1
	if 'e' not in wyraz:
		print(wyraz)
		procent += 1
print (calosc)
print (procent)
print ((100 * procent ) / calosc)
