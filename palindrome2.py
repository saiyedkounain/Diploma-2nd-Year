def is_palindrome(n):
    rev=0
    temp=n
    while temp>0:
        rem=temp%10
        rev=rev*10+rem
        temp=temp//10
    if rev==n:
        return True
    else:
        return False
num=int(input("Enter yo: "))
if is_palindrome(num):
    print(f"Yes, {num} is a palindrome")
