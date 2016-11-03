def partition(a, low, high):
    key = a[low]
    left = low+1
    right = high
    while left <= right:
        while left <= right and a[left] <= key: left = left + 1
        while left <= right and a[right] >= key: right = right-1
        if left <= right:
            temp = a[left]
            a[left] = a[right]
            a[right] = temp
    a[low] = a[right]
    a[right] = key
    return right

def QuickSort(a, lowIndex, highIndex):
    if highIndex > lowIndex:
        splitIndex = partition(a,lowIndex,highIndex)
        #print("splitIndex =", splitIndex)
        QuickSort(a,lowIndex,splitIndex-1)
        QuickSort(a,splitIndex+1,highIndex)

def dataOfSize(n):
    import random
    rng = random.Random()
    rv = []
    for i in range(n):
        rv.append(rng.randrange(0,2*n))
    return rv

if __name__ == "__main__":
    unsorted = dataOfSize(200)
    test = unsorted.copy()
    QuickSort(test, 0, len(test)-1)
    print("Unsorted:", unsorted)
    print("Sorted:",test)
