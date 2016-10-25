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

def selectionSort(list):
	for j in range(len(list)-1,0,-1):
		aMax=0
		for k in range(1,j+1):
			if list[k]>list[aMax]:
				aMax=k
		temp=list[j]
		list[j]=list[aMax]
		list[aMax]=temp
	return(list)

def quickSort(alist):
       quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:
       splitpoint = partition(alist,first,last)
       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


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

#function to create list given by Yeager
def dataOfSize(n):
    import random
    rng=random.Random()
    rv=[]
    for i in range(n):
        rv.append(rng.randrange(0,2*n))
    return rv

fout=open("hw4.txt","w")
import time
import random

def main():
	count=0
	while count <= 1000:
		count+=1
		xyz=random.randint(100,1000)
		aList=dataOfSize(xyz)
		N=len(aList)
		#bubble sort section
		bStart=time.time()
		bubble=bubbleSort(aList)
		bN=time.time()-bStart
		#selection sort section
		sStart=time.time()
		selection=selectionSort(aList)
		sN=time.time()-sStart
		#quick sort section
		qStart=time.time()
		quick=quickSort(aList)
		qN=time.time()-qStart
		#print(bN)
		#print(sN)
		#print(qN)
		output=(str(N) + "\t" + str(bN) + "\t" + str(sN) + "\t" + str(qN) + "\n")
		fout.write(output)

main()
fout.close()