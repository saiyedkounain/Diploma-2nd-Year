#binary search
ls = [1,2,3,4,5]
key = 4
n = len(ls)
low = 0
high = n-1
flag =0
while (low <=high):
    mid = (high+low)//2
    if ls[mid] == key:
        flag =1
        break
    elif ls[mid] > key:
        high = mid-1
    else:
        low = mid+1
if flag ==1:
    print("Element found!")
else:
    print("Element not found!")
