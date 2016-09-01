import time
import math
import os
import random

def main():
	
	i=0
	size=10
	a=[]

	a=[0 for i in range(size)]
	
	for i in range(size):
		a[i]=i
		i+=1

	print(a)


	zeta=random.shuffle(a)

	print(zeta)



main()
