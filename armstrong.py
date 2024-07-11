#armstrong number in  rnage
start=int(input("Enter stafrt: "))
end=int(input("Enter emd:"))
for n in range(start,end+1):
    sum=0
    temp=n
    while temp>0:
        digit=temp%10
        sum=sum+digit**3
        temp=temp//10
    if n==sum:
        print(n)
