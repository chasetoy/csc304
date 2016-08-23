import random
import time
import math

def selection(aList):
	for j in range(len(aList)-1,0,-1):
		aMax=0
		for k in range(1,j+1):
			 if aList[k]>aList[aMax]:
				 aMax = k

		temp = aList[j]
		aList[j] = aList[aMax]
		aList[aMax] = temp

	print(aList)


def main():
	a=[]
	i=[]
	size=10

	a=[ 0 for i in range (size)]

	for i in range(size):
		a[i]=i
		i+1

	print(a)

	selection(a)

	return(a)

main()
