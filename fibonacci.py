n=int(input("Enter the number of nterms: "))
f=0
s=1
if n<=f:
    print("The fibanacci sequence is", f)
else:
    print(f,s,end="")
    for i in range(2,n):
        t=f+s
        print(t,end="")
        f=s
        s=t
