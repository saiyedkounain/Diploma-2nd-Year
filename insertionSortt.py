# insertion sort
ls =[5,3,4,2,1]
n = len(ls)
print("Marks before: ",ls)
for i in range(1,n):
    current = ls[i]
    j=i-1

    while(j>=0 and current < ls[j]):
        ls[j+1] = ls[j]
        j-=1

        ls[j+1] = current

print ("Marks After: ",ls)
