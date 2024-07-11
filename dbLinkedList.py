#Double Linked List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class dbLinkedList:
    def __init__(self):
        self.head = None
    def addFirst(self,data):
        newNode = Node(data)
        if (self.head == None):
            self.head = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
    def delLast(self):
        if (self.head == None):
            print("Empty Linked List")
        elif (self.head.next == None):
            self.head = None
        else:
            currNode = self.head
            while (currNode.next != None):
                currNode = currNode.next
            currNode.prev.next = None

    def printList(self):
        currNode = self.head
        while (currNode != None):
            print("<-",currNode.data, "->", end="")
            currNode = currNode.next
        print("null")
db = dbLinkedList()
db.addFirst("IDK")
db.addFirst("Kounain")
db.addFirst("Saiyed")
db.addFirst("Not")
db.delLast()
db.printList()


