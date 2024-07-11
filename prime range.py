start= int(input("Enter: "))
end = int(input("Enter: "))
for n in range(start,end):
    flag = 0
    for i in range (2,n):
        if (n%i==0):
            flag=1
    if flag==0:
        print(n)
    
