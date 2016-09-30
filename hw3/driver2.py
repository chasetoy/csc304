# chase toy
# csc 304
# homework 3
# 09/22/16

fout = open("triples2.txt","w")
from Transpose import transpose
from Transpose import makeTranspose
import time
from random import Random
import random
startTime = time.time()
def main():
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
    
    r1=random.randint(100,500)
    r2=random.randint(500,1000)
    print(r1)
    print(r2)
    kList=a[r1:r2]
    print(kList)

main()
fout.close()
