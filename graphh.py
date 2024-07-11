#plotting a graph
import time
import numpy as np
import matplotlib.pyplot as plt
def bubbleSort(ls):
    n=len(ls)
    for i in range(0, n-1):
        for j in range(0,n-i-1):
            if(ls[j] > ls[j+1]):
                ls[j],ls[j+1] = ls[j+1], ls[j]
    return ls

ls=[8,2,3,1,4]
print("Sorted List: ",bubbleSort(ls))

#plotting graph
elements = np.array([i*500 for i in range(1,5)])
print("Number of elements: ",elements)
times = list()
for i in range(1,5):
    a = list(np.random.randint(500,size=(i*500)))
    s = time.time()
    bubbleSort(a)
    e = time.time()
    times.append(e-s)
    print("Time taken to sort ", len(a), "elements: ", e-s,"s")
plt.plot(elements,times,color='r', label="Bubble Sort")
plt.xlabel("Number of Elements")
plt.ylabel("Time Taken")
plt.legend()
plt.grid()
plt.show()
