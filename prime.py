def is_prime(n):
    flag=0
    for i in range (2,n):
        if n%i ==0:
            flag=1
        else:
            pass
    if flag==0:
        return True
    else:
        return False
