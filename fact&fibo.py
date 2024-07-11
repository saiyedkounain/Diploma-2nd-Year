#fibonacci recursive and factorial of 7
def fact(n):
    if n <= 1:
        return n
    else:
        return n*fact(n-1)
def fibo(n):
    if n<= 1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
num=7
print(f"The factorial of {num} is",fact(num))
for i in range (2,num):
    print(f"The fibonacci of {num} terms:", fibo(i))
