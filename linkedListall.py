#Linked List All operations
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def addFirst(self,data):
        ptr = Node(data)
        if (self.head == None):
            self.head = ptr
        else:
            ptr.next = self.head
            self.head = ptr
    def addLast(self,data):
        ptr = Node(data)
        if (self.head == None):
            self.head = ptr
        else:
            temp = self.str
            while(temp.next != None):
                temp = temp.next
            temp.next = ptr
    def printList(self):
        if (self.head == None):
            print("Empty List")
        else:
            temp = self.head
            while(temp != None):
                print(temp.data, "->", end="")
                temp = temp.next
    def delFirst(self):
        if (self.head == None):
            return
        else:
            self.head = self.head.next
    def delLast(self):
        if (self.head == None):
            return
        elif (self.head.next == None):
            self.head = None
        else:
            temp = self.head
            while(temp.next.next != None):
                temp = temp.next
            temp.next = None
ll = LinkedList()
#driver code'
print("1.To Add First 2.Add Last 3.Delete First 4.Delete Last 5. Display 6.Exit")
while True:
    ch = int(input("Enter your choice: "))
    if ch ==1:
        data = int(input("Enter value to add at first: "))
        ll.addFirst(data)
        print(data," has been added")
    elif ch==2:
        data = int(input("Enter value to add at last: "))
        ll.addFirst(data)
        print(data," has been added")
    elif ch==3:
        ll.delFirst()
        print("First Item Deleted")
    elif ch==4:
        ll.delLast()
        print("Last Item Popped")
    elif ch==5:
        ll.printList()
    elif ch==6:
        break
    else:
        print("Invalid Option")
