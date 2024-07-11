import time
def lns(ls,key):
    n = len(ls)
    flag =0
    for i in range(0,n):
        if ls[i] == key:
            flag = 1
    if(flag == 1):
        print("Element Found")
    else:
        print("Element not found")
def bns(ls,key):
    flag = 0
    low =0
    high = len(ls)-1
    while(low <= high):
        mid = (high+low)//2
        if (ls[mid] == key):
            flag = 1
            break
        elif (ls[mid] > key):
            high = mid-1
        else:
            low = mid+1
    if (flag ==1):
        print("Element Found")
    else:
        print("Element not found!")
        
ls = [1,2,5,8,9]
print("*** 1.Linear Search,  2.Binary Search,   3.Quit ***")
while True:
    ch = int(input("Enter your choice: "))
    if ch==1:
        key = int(input("Enter key to find: "))
        print("Linear Search")
        s = time.time()
        lns(ls,key)
        e = time.time()
        print("Time taken: ", s-e)
    elif ch==2:
        key = int(input("Enter key to find: "))
        print("Binary Search, only for sorted lists")
        s = time.time()
        bns(ls,key)
        e = time.time()
        print("Time taken: ", s-e)
    elif ch==3:
        break
    
