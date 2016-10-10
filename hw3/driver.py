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
		start1 = time.time()
		a1 = makeTranspose(a)
		t1 = time.time() - start1
		start2 = time.time()
		a2 = transpose(a)
		t2 = time.time() - start2
		numRow = len(a)
		numCol = len(a[0])
		N = str(numRow) + "X" + str(numCol)
	#	print(a1)
		print(N)
		print(t1)
		print(t2)
		output = str(N + "\t" + str(t1) + "\t" + str(t2) + "\n")
		fout.write(output)

main()
fout.close()
