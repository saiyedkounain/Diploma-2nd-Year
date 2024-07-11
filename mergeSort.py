def mergeSort(ls):
    if len(ls) >1:
        n = len(ls)//2
        L = ls[:n]
        R = ls[n:]


        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                ls[k] = L[i]
                
                i+=1
            else:
                ls[k] = R[j]
                
                j+=1
        k+=1

        while i < len(L):
            ls[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            ls[k] = R[j]
            j+=1
            k+=1

def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()

#stuff
arr = [6,2,3,1,9]
mergeSort(arr)
printList(arr)

