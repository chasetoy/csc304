# chase toy
# csc 304
# homework 3
# 09/22/16

fout = open("triples.txt","w")
from Transpose import transpose
from Transpose import makeTranspose
import time
from random import Random
startTime = time.time()
def main():
	a=[]
	b=[]
	size=1
	size2=10
	i=1
	count=0
	while count != 1000:
		for i in range(size, size2):
			for j in range(size, size2):
				b.append(i)
			a.append(b)
			b=[]
		count+=1
		a1 = makeTranspose(a)
		t1 = time.time() - startTime
		a2 = transpose(a)
		t2 = time.time() - startTime
		numRow = len(a)
		numCol = len(a[0])
		N = str(numRow) + "X" + str(numCol)
		print(count)
		print("N = ", N)
		print("T(n) = ", t1, "seconds.")
		print("M(n) = ", t2, "seconds.")
		print(" ")
		output = str(N + "\t" + str(t1) + "\t" + str(t2) + "\n")
		fout.write(output)

main()
fout.close()