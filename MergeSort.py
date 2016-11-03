def MergeSort(ell):
    if len(ell) <= 1: return
    else:
        mid = len(ell) // 2
        ell1 = ell[0:mid]
        ell2 = ell[mid:len(ell)]
        MergeSort(ell1)
        MergeSort(ell2)
        ell[0:] = merge(ell1,ell2)

def merge(ell1, ell2):
    i = j = 0
    mergedList = []
    while i in range(len(ell1)) and j in range(len(ell2)):
        if ell1[i] <= ell2[j]:
            mergedList.append(ell1[i])
            i += 1
        else:
            mergedList.append(ell2[j])
            j += 1
    if i < len(ell1):
        mergedList = mergedList + ell1[i:len(ell1)]
    elif j < len(ell2):
        mergedList = mergedList + ell2[j:len(ell2)]
    return mergedList

if __name__ == "__main__":
    trial = [29,72,34,58,61,38]
    MergeSort(trial)
    print(trial)
    
