#Bubble SOrt
ls = [1,5,4,2,6,7,3]
n = len(ls)

for i in range(0,n-1):
    swap =0
    for j in range (1, n-i-1):
        if(ls[j] > ls[j+1]):
            swap += 1
            #swap
            ls[j],ls[j+1] = ls[j+1],ls[j]
    if swap == 0:
        print("Breaking now")
        break

print(ls)
