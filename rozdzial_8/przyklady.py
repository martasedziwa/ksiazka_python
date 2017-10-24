def od_konca(s):
	i = -1
	while i > -(len(s)+1):
		print (s[i])
		i -= 1
		



def nazwiska():
	n = 'JKLMNOPQ'
	s = 'ack'
	for i in n:
		if i == 'O' or i == 'Q':
			print (i+'u'+s)
		else:
			print (i +s)


def find(wyraz, litera, poczatek): #sprawdza polozenie znaku w lancuchu
	index = poczatek
	print (len(wyraz))
	while index < len(wyraz):
		if wyraz[index] == litera:
			print (index)
			return (index)
		index += 1
	print ('-1')
	return -1

def count(wyraz, litera):  #find == count - liczy ile razy wystepuje podany znak w podanym lancuchu
	count = 0
	for l in wyraz:
		if litera == l:
			count += 1
	print (count)
	



def find(wyraz, litera, poczatek):
	index = poczatek
	count = 0
	while index < len(wyraz):
		if wyraz[index] == litera:
			count += 1
		index += 1
	print (count)
	


def is_reverse(wyraz1, wyraz2):
	if len(wyraz1) != len(wyraz2):
		print ('False')
		return False
	j = len(wyraz2)-1
	i = 0
	while i < len(wyraz1):
		print(i, j)
		if wyraz1[i] != wyraz2[j] :
			print ('False')
			return False
		i += 1
		j -= 1
	print ('True')
	return True
		



def is_palindrome(wyraz1, wyraz2):
	if wyraz1[:] == wyraz2[::-1]:
		print('palindrom')
		return True
	print ('nie')
	return False

def any_lowercase(wyraz):
	for c in wyraz:
		if not c.islower():
			print('false')
			return False
			
	print ('true')
	return True
		
any_lowercase('aARtA')
