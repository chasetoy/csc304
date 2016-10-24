#chase toy
#csc 304
#hw4: bubble sort and times


def bubbleSort(list):
	for k in range(len(list)-1,0,-1):
		for i in range(k):
			if list[i]>list[i+1]:
				temp=list[i]
				list[i]=list[i+1]
				list[i+1]=temp
	return(list)


def main():
	a=[1,5,3,6,7,5,4,3,5,7,8,89,7,6,656,55,354]
	a1=bubbleSort(a)
	print(a1)

main()
