class LinkedList:
    class  Node:
        #constructor
        def __init__(self,data):
            self.data = data
            self.next = None
    #Constructor for linked list
    def __init__(self):
        self.head = None

    
    def addFirst(self,data):
        newNode = self.Node(data)
        if (self.head == None):
            self.head = newNode
            return
        
        newNode.next = self.head
        self.head = newNode
    
    def addLast(self, data):
        newNode = self.Node(data)
        if (self.head == None):
            self.head = newNode
            return
        currNode = self.head

        while (currNode.next != None):
            currNode = currNode.next
        
        currNode.next = newNode

    def printList(self):
        if (self.head == None):
            print("Empty Linked List")
        
        currNode = self.head

        while (currNode != None):
            print(currNode.data,"->", end="")
            currNode = currNode.next
        print("None")
        
#driver main function
list = LinkedList()
list.addFirst("Saiyed")
list.addLast("Kounain")
list.printList()

