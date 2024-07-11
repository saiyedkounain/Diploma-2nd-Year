#selection sort
marks= [5,3,4,2,1,6]
print ("Before Selection Sort: " ,marks)
for i in range (0,len(marks)-1):
    smallest = i
    for j in range (i+1, len(marks)):
        if (marks[smallest]>marks[j]):
            print(marks[smallest],">",marks[j])
            smallest = j
    # swap now
    marks[smallest],marks[i] = marks[i],marks[smallest] 

print("After Selection Sort: " ,marks)
        
