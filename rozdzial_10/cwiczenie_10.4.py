def main():
	t =[1,2,3,4,5]
	chop(t)
	print (t)

def chop(t):
	del t[1]
	del t[len(t)-1]
	return (None)

main()
