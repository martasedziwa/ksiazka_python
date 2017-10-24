def main():
	t = [3,5,6,5,2,3,4,8]
	print (middle(t))

def middle(t):
	nowa_lista = []
	nowa_lista.append(t[1:len(t)-1])
	return(nowa_lista)

main()
