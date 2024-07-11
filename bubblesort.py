# Bubble sort prolly
import time
sk = [4,5,3,2,1]
print("Before bubble sort: ",sk)

s = time.time()
for i in range(0,len(sk)-1):
    for j in range (0,len(sk)-1-i):
        if (sk[j]>sk[j+1]):
            #swap
            sk[j], sk[j+1] = sk[j+1], sk[j]
e = time.time()

print ("After bubble sort",sk)
print("Time taken: ", e-s)
