#Stack in Linked List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    #stack adding at last
    def push(self,data):
        ptr = Node(data)
        if (self.head == None):
            self.head = ptr
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = ptr
    #stack removing at end
    def popItem(self):
        if (self.head == None):
            print("Empty List")
        elif(self.head.next == None):
            self.head = None
        else:
            temp = self.head
            while (temp.next.next != None):
                temp = temp.next
            temp.next = None
    def display(self):
        if (self.head == None):
            print("Empty List")
        else:
            temp = self.head
            while (temp != None):
                print(temp.data, "->")
                temp = temp.next
            
#driver code
ll = LinkedList()
print("Select 1.Push 2.Pop 3.Display 4.Exit")
while True:
    ch = int(input("Enter your choice: "))
    if ch==1:
        data = int(input("Enter value to add"))
        ll.push(data)
        print(data," has been added")
    elif ch==2:
        ll.popItem()
        print("Item Popped")
    elif ch==3:
        ll.display()
    elif ch==4:
        break
    else:
        print("Invalid Operation")

        
