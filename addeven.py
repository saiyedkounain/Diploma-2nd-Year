#addition of even numbers
n=int(input("Enter yo:"))
sum=0
for i in range(n+1):
    if i%2 ==0:
        sum = sum+i
        print(i)
print("The sum of these numbers is",sum)
