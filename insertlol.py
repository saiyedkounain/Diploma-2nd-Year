#insertion Sort
def sort_ascending(ls):
    #Implementing Insertion Sort
    for i in range (1, len(ls)):
        current = ls[i]
        j = i-1
        while (j >=0 and current < ls[j]):
            ls[j+1] = ls[j]
            j = j-1

        #placement
        ls[j+1] = current
    print("Sorted list")
    print(ls)
def sort_descending(ls):
    #Implementing bubble sort for descending
    n = len(ls)
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if (ls[j] < ls[j+1]):
                #swap
                temp = ls[j]
                ls[j] = ls[j+1]
                ls[j+1] = temp
    print("Descended Sorting: ", ls)
    
    
marks = []
print("Enter 5 numbers  and this program will sort them  in order:")
for i in range(0,5):
    el= int (input("Enter the element: "))
    marks.append(el)
tempmarks = marks.copy()
print("Your list")
print(marks)

while True:
    print("Enter 1: Sort Ascending 2: Sort Descending: 3.To Display Original List 4.To Quit")
    ch = int(input("Select: "))
    if ch==1:
        sort_ascending(marks)
    elif ch==2:
        sort_descending(marks)
    elif ch == 3:
        print(tempmarks)
    elif ch ==4:
        break
    else:
        print("Invalid Operation")
            



