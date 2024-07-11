#perfect number
start=int(input("Enter start: "))
end=int(input("Enter end: "))
for n in range(start,end+1):
    sum=0
    for i in range(1,n):
        if n%i == 0:
            sum=sum+i
        else:
            pass
    if sum == n:
        print(n)
            
