# Student Record Management using basic data structure

def display():
    print("Name: ",name)
    print("Roll no: ",rn)
    print("Marks 1: ",m1)
    print("Marks 2: ",m2)
    print("Marks 3: ",m3)
    print("Marks 4: ",m4)
    total = m1+m2+m3+m4
    print("Total: ",total)
def result():
    total = m1+m2+m3+m4
    print((total/400)*100, "%")
def search():
    m = [m1,m2,m3,m4]
    n = int(input("Enter marks to find: "))
    for i in m:
        if i == n:
            print("Marks found at ",i )
        else:
            print("Marks not found!")



#read
name =input("Enter name: ")
rn = int(input("Enter roll no: "))
m1 = int(input("Enter marks: "))
m2 = int(input("Enter marks: "))
m3 = int(input("Enter marks: "))
m4 = int(input("Enter marks: "))
while True:
    print("Select 1. To Display 2.To Search 3.To Calculate Result 4.To Quit")
    ch = int(input("Enter your choice: "))
    if ch==1:
        display()
    elif ch==2:
        search()
    elif ch==3:
        result()
    elif ch==4:
        break
