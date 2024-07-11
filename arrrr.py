#insertion Sort lol
arr = [9,8,7,6,5,4,3,1,2]
for i in range (1, len(arr)):
    current = arr[i]
    j = i-1
    while (j>=0 and current < arr[j]):
        arr[j+1] = arr [j]
        j = j-1
    #placement
    arr [j+1] = current
print(arr)
