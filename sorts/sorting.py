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
		size=random.randint(100,100)

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

	def quickSortHelper(alist,first,last):
		if first<last:
			splitpoint = sort.partition(alist,first,last)
			sort.quickSortHelper(alist,first,splitpoint-1)
			sort.quickSortHelper(alist,splitpoint+1,last)


	def partition(alist,first,last):
		pivotvalue = alist[first]
		leftmark = first+1
		rightmark = last
		done = False
		while not done:
			while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
				leftmark = leftmark + 1
			while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
				rightmark = rightmark -1
			if rightmark < leftmark:
				done = True
			else:
				temp = alist[leftmark]
				alist[leftmark] = alist[rightmark]
				alist[rightmark] = temp
		temp = alist[first]
		alist[first] = alist[rightmark]
		alist[rightmark] = temp
		return rightmark

	def quickSort(alist):
		sort.quickSortHelper(alist,0,len(alist)-1)

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
			done=sort.quickSort(fin)
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

fout=open("sort.txt","w")

def main():

	count=0
	xyz=random.randint(100,200)
	while count != 1000:
		widow=sort
		xyz+=1
		count+=1
		
		odin=widow.init(list, xyz)
		zeta=widow.make(odin)
		#print("init     : ", zeta)
		#print()

		widow.shuffle(zeta)
		#print("shuffled : ", zeta)
		#print()

		iStart=time.time()
		newZeta=widow.insertion(zeta)
		#print("insertion: ", newZeta)
		iN=time.time()-iStart
		#print()

		widow.shuffle(zeta)
		sStart=time.time()
		zetaPrime=widow.selection(zeta)
		sN=time.time()-sStart
		#print("selection: ", zetaPrime)
		#print()

		widow.shuffle(zeta)
		bStart=time.time()
		omega=widow.bubble(zeta)
		bN=time.time()-bStart
		#print("bubble   : ", omega)
		#print()

		widow.shuffle(zeta)
		cStart=time.time()
		chase=widow.cSort(zeta)
		cN=time.time()-cStart
		#print("cSort    : ", chase)

		widow.shuffle(zeta)
		qStart=time.time()
		quick=widow.quickSort(zeta)
		qN=time.time()-qStart

		output=(str(xyz) + "\t" + str(iN) + "\t" + str(sN) + "\t" + str(bN) + "\t" + str(cN) + "\t" + str(qN) + "\n")
		fout.write(output)

	print("DONE")

main()
