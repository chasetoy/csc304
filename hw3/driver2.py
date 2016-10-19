# chase toy
# csc 304
# homework 3
# 09/22/16

import time
fout = open("driver2.txt","w")

def makeArray(n):
    list=[]
    for i in range(n):
        list.append([1]*n)
    return list

def main():
    n=20000
    k=5000
    list=makeArray(2*n)
    while k<=n:
        start1=time.time()
        c=list[100:k+100]
        T_k=time.time()-start1
        fout.write("%d\t%e\n"%(k,T_k))
        k=k+100

main()
