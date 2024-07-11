# Bubble sort prolly
sk = [4,5,3,2,1]
print("Before bubble sort: ",sk)

for i in range(0,len(sk)-1):
    for j in range (0,len(sk)-1-i):
        if (sk[j]>sk[j+1]):
            #swap
            temp = sk[j]
            sk[j] = sk[j+1]
            sk[j+1] = temp

print ("After bubble sort",sk)
