#factorial while loop or for loop
n=int(input("Enter nterms: "))
fact=1
temp=n
for i in range (1,n):
    fact=fact*n
    n=n-1
print(f"The factorial of {temp} is {fact}")
