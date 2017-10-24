def main():
	t = [1,2,3]
	print(cumsut(t))

def cumsut(t):
	nowa_lista = []
	for i in range (0,len(t)):
		nowa_lista.append(sum(t[0:i+1]))
	return (nowa_lista)

main()
