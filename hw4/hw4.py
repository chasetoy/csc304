#chase toy
#csc 304
#hw4: bubble sort, selection sort, quick sort and time graphs


def bubbleSort(alist):
	for k in range(len(alist)-1,0,-1):
		for i in range(k):
			if alist[i]>alist[i+1]:
				temp=alist[i]
				alist[i]=alist[i+1]
				alist[i+1]=temp
	return(alist)

def selectionSort(alist):
	for j in range(len(alist)-1,0,-1):
		aMax=0
		for k in range(1,j+1):
			if alist[k]>alist[aMax]:
				aMax=k
		temp=alist[j]
		alist[j]=alist[aMax]
		alist[aMax]=temp
	return(alist)

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

def shuffle(alist):
    		import random
		random.shuffle(alist)
		return(alist)

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
	xyz=random.randint(100,200)
	#alist=dataOfSize(xyz)
	while count != 1000:
		xyz+=1
		count+=1
		alist=dataOfSize(xyz)
		N=len(alist)
		#bubble sort section
		bubble=shuffle(alist)
		bStart=time.time()
		bubble=bubbleSort(bubble)
		bN=time.time()-bStart
		#selection sort section
		selection=shuffle(alist)
		sStart=time.time()
		selection=selectionSort(selection)
		sN=time.time()-sStart
		#quick sort section
		quick=shuffle(alist)
		qStart=time.time()
		quick=quickSort(quick)
		qN=time.time()-qStart
		output=(str(N) + "\t" + str(bN) + "\t" + str(sN) + "\t" + str(qN) + "\n")
		fout.write(output)

main()
fout.close()