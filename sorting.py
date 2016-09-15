import random
import time
import math
import os

class sort():

	def disp(list):
		print()
		print(list)
		print()

	def getSize():
		import random
		size=random.randint(10000,10000)

		return(size)

	def init(list, size):
		i=0
		list=[0 for i in range(size)]
		return(list)

	def make(list):
		size=len(list)
		i=0
		for i in range(size):
			list[i]=i
			i+=1
		return(list)

	def shuffle(list):
		import random
		random.shuffle(list)
		return(list)

	def insertion(list):
		for i in range(1,len(list)):

			tesla=list[i]
			k=i

			while k>0 and list[k-1]>tesla:
				list[k]=list[k-1]
				k=k-1

			list[k]=tesla

		return(list)



	def selection(aList):
		for j in range(len(aList)-1,0,-1):
			aMax=0
			for k in range(1,j+1):
			 	if aList[k]>aList[aMax]:
				 	aMax=k

			temp=aList[j]
			aList[j]=aList[aMax]
			aList[aMax]=temp

		return(aList)

	def bubble(list):
		for k in range(len(list)-1,0,-1):
			for i in range(k):
				if list[i]>list[i+1]:
					temp=list[i]
					list[i]=list[i+1]
					list[i+1]=temp
		return(list)

	def cSort(list):
		if len(list)>1:
			mid=len(list)//2
			lft=list[:mid]
			rgt=list[mid:]

			sLft=sort.insertion(lft)
			sRgt=sort.insertion(rgt)

			fin=sLft+sRgt
			done=sort.insertion(fin)
		return(done)

	def chunk(list):
		if len(list)>1:
			mid=len(list)//2
			lft=list[:mid]
			rgt=list[mid:]

			while(mid>5):
				sort.chunk(lft)
				sort.chunk(rgt)

		return(lft, rgt)



def main():

	widow=sort

	size=widow.getSize()
	print()
#	print("SIZE      : ", size)
	print()

	odin=widow.init(list, size)
	zeta=widow.make(odin)
#	print("init     : ", zeta)
	print()

	widow.shuffle(zeta)
#	print("shuffled : ", zeta)
	print()

	newZeta=widow.insertion(zeta)
#	print("insertion: ", newZeta)
	print()

	widow.shuffle(zeta)
	zetaPrime=widow.selection(zeta)
#	print("selection: ", zetaPrime)
	print()

	widow.shuffle(zeta)
	omega=widow.bubble(zeta)
#	print("bubble   : ", omega)
	print()

	widow.shuffle(zeta)
	chase=widow.cSort(zeta)
#	print("cSort    : ", chase)

	print("DONE")

main()
