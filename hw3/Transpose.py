def makeTranspose(A):
	for i in range(len(A)-1):
		for j in range(i+1,len(A[i])):
			temp = A[i][j]
			A[i][j] = A[j][i]
			A[j][i] = temp
	return(A)

def transpose(A):
    B = list()
    for col in range(len(A[0])):
        B.append(list())
        for row in range(len(A)):
            B[col].append(A[row][col])
    return B

if (__name__ == "__main__"):
    
    def main():
        test1 = [[1,1,1], [2,2,2], [3,3,3]]
        test2 = [[5, 6, 7], [0, 2, 1], [9, -3, 6], [8, 9, 10]]     
        print("The transpose of ")
        print(test1)
        print("is")
        makeTranspose(test1)
        print(test1)
        print()
        print("The transpose of ")
        print(test2)
        print("is")
        print(transpose(test2))
 
    main()
    


