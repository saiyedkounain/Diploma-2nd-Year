#Recursive Factorial
def recur_fact(n):
    if n<=1:
        return n
    else:
        return n*recur_fact(n-1)
num=7
print(f"The factorial of {num} is",recur_fact(num))
