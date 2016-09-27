import random
import time
import math

def main():
    a=[]
    size=5
    size2=3
    i=0
    count=0
    while count != 1000:
        for x in range(size):
            a.append([])
            for y in range(size2):
                a[x].append(i)
        i+=1
        count+=1

    print(a)

main()