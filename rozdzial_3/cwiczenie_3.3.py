def siatka1():
	print(('+'+'-'*4)*2+'+')  #print(('+'+'-'*4)*4+'+')  do punktu 2

def siatka2():
	print((('|'+' '*4)*2+'|'))  #print((('|'+' '*4)*4+'|'))  do punktu 2

def siatka3(obiekt_funkcji):
	obiekt_funkcji()
	obiekt_funkcji()
	obiekt_funkcji()
	obiekt_funkcji()	
	
	
siatka1()
siatka3(siatka2)
siatka1()
siatka3(siatka2)
siatka1()
siatka3(siatka2)
siatka1()
siatka3(siatka2)
siatka1()

