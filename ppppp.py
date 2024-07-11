n=int(input("Enter number:"))
flag=0
for i in range (2,n):
    if n%i ==0:
        flag=1
    else:
        pass
if flag==0:
    print(f"Yes, {n} is a prime number")
else:
    print("Not a prime number")
