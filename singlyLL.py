#singly linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def addFirst(self,data):
        newNode = Node(data)
        if (self.head == None):
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    def addLast(self,data):
        newNode = Node(data)
        if (self.head == None):
            newNode = self.head
        else:
            currNode =self.head
            while(currNode.next != None):
                currNode = currNode.next
            currNode.next = newNode
    def printList(self):
        if (self.head == None):
            print("Empty")
        else:
            currNode =self.head
            while(currNode != None):
                print(currNode.data, "->", end="")
                currNode = currNode.next
            print("null")
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
            
            secondLastNode = self.head
            while (secondLastNode.next.next != None):
                secondLastNode = secondLastNode.next
            secondLastNode.next = None
            
ll = LinkedList()
ll.addFirst(54)
ll.addLast(67)
ll.delLast()
ll.printList()


            
