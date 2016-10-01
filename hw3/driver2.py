# chase toy
# csc 304
# homework 3
# 09/22/16

fout = open("triples.txt","w")
fout2= open("triples2.txt","w")
from Transpose import transpose
from Transpose import makeTranspose
import time
#from random import Random
import random
startTime = time.time()
def main():
    r1=random.randint(100,500)
    r2=random.randint(500,1000)
    a=[]
    b=[]
    size=1
    size2=2
    size3=3
    size4=4
    i=1
    count=0
    while count != 1000:
        for i in range(size, size2):
            for j in range(size, size2):
                b.append(i)
                a.append(b)
        size+=1
        size2+=1
        count+=1
        a1 = makeTranspose(a)
        t1 = time.time() - startTime
        a2 = transpose(a)
        t2 = time.time() - startTime
        numRow = len(a)
        numCol = len(a[0])
        N = str(numRow) + "X" + str(numCol)
        print(N)
        print(t1)
        print(t2)
        output = str(N + "\t" + str(t1) + "\t" + str(t2) + "\n")
        fout.write(output)
    kList=a[r1:r2]
    #print(kList)
    #r1=random.randint(100,500)
    #r2=random.randint(500,1000)
    nr=len(kList)
    nc=len(kList[0])
    #n=nr*nc
    count2=r1
    startTime2 = time.time()
    while count2 < r2:
        #k2=kList
        k3 = makeTranspose(kList)
        t3 = time.time() - startTime2
        k4 = transpose(kList)
        t4 = time.time() - startTime2
        count2+=1
        n = str(nr) + "X" + str(nc)
        print(n)
        print(t3)
        print(t4)
        output = str(n + "\t" + str(t3) + "\t" + str(t4) + "\n")
        fout.write(output)

main()
fout.close()
fout2.close()
