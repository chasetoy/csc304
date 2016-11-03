from time import clock
from MergeSort import MergeSort
from QuickSort import QuickSort

def SelectionSort(ell):
    for i in range(len(ell)-1):
        min_i = i
        for j in range(len(ell)):
            if ell[j] < ell[min_i]: min_i = j
        temp = ell[i]
        ell[i] = ell[min_i]
        ell[min_i] = ell[i]
        
class MaxHeap:
    def __init__(self,alist=[]):
        self.values = [None] + alist
        self.n = len(self.values)-1
        j = self.n//2
        while j >= 1:
            self.percDown(j)
            j = j-1
    def insertInHeap(self,value):
        self.values.append(value)
        self.percUp(len(self.values)-1)
    def __str__(self):
        return str(self.values[1:])
    def percDown(self,i):
        finished = i > self.n//2
        while not finished:
            left = 2*i
            right = left+1
            maxIndex = left
            if right <= self.n:
                if self.values[right] > self.values[maxIndex]:
                    maxIndex = right
            if maxIndex > self.n or self.values[maxIndex] < self.values[i]:
                finished = True
            else:
                temp = self.values[i]
                self.values[i] = self.values[maxIndex]
                self.values[maxIndex] = temp
                i = maxIndex
    def sort(self):
        while self.n > 1:
            temp = self.values[self.n]
            self.values[self.n] = self.values[1]
            self.values[1] = temp
            self.n = self.n - 1
            self.percDown(1)
        self.n = len(self.values)-1

if __name__ == "__main__":
    import random
    rng = random.Random()
    for testSize in range(20,1000,20):
        origList = [rng.randrange(testSize*2) for i in range(testSize)]

        testList = origList + []
        then = clock()
        myHeap = MaxHeap(testList)
        myHeap.sort()
        hsTime = clock() - then
        
        testList = origList + []
        then = clock()
        QuickSort(testList,0,len(testList)-1)
        qsTime = clock() - then
        
        testList = origList + []
        then = clock()
        MergeSort(testList)
        msTime = clock() - then
        
        print(str(testSize)+'\t'+str(hsTime)+'\t'+str(qsTime)+'\t'+str(msTime))
        """
        testList = origList + []
        then = clock()
        SelectionSort(testList)
        ssTime = clock() - then
        
        print(str(testSize)+'\t'+str(hsTime)+'\t'+str(qsTime)+'\t'+str(ssTime))
        """
