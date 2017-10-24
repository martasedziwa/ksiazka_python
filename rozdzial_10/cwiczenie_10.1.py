def main():
	t = [[1,2,3],[4,5,6],[7,8]]
	print (nested_sum(t))

def nested_sum(t):
	suma = 0
	for i in range(0,len(t)):
		suma +=  sum(t[i])
	return (suma)	

main()
