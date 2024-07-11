#bubble sort
arr = [5,4,3,2,1]
print("Before: ",arr)
for i in range(0,len(arr)-1):
    for j in range (0, len(arr)-1-i):
        if (arr[j] > arr[j+1]):
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
print("After: ",arr)
            
