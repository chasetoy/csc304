def main():

	inFile = open("varLenData.txt", "r")
	a=[]
	b= set(open("varLenData.txt").read().strip().split())
	print("unsorted set")
	print(b)
	b1=sorted(b)
	print("sorted set")
	print(b1)

main()
