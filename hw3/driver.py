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
	size = 1000
	count = 0
	for i in range(size):
		count += 1
		a = [[1,1,1],[2,2,2],[3,3,3]]
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
		output = str(str(t1) + "\t" + str(t2) + "\n")
		fout.write(output)

main()
fout.close()
