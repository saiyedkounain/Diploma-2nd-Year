#Recursive Fibonacci
def rec_fibo(n):
    if n==0 or n==1:
        return n
    else:
        return rec_fibo(n-1)+rec_fibo(n-2)
num=15
if num <= 0:
    print("Enter positive n terms")
else:
    for i in range(2,num):
      print (rec_fibo(i))
