def is_palindrome(n):
    rev=0
    temp=n
    while n>0:
        rem=n%10
        rev=rev*10+rem
        n=n//10
    if rev==temp:
        return True
    else:
        return False

num=1221
if is_palindrome(num):
    print("Yes, its a palindrome, mt friend!")

