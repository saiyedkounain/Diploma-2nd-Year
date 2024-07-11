# Removing Duplicates from Linked List
#Implementing a linked list

def printThroughHead(head):
    curr = head
    
    while curr != None :
        print(curr.val , " -> ", end="")
        curr = curr.next
def deleteDuplicates(head):
    if head == None :
        return head

    dummy = Node("Dummy")
    dummy.next = head

    #definojg pointers
    prev = dummy
    curr = head

    while (curr != None):
        if (curr.val != curr.next.val):
            prev = prev.next
            curr = curr.next
        else:
            while(curr.val != curr.next.val):
                curr = curr.next
            prev.next = curr.next

    return dummy.next
class LinkedList:

    def __init__(self,head):
        self.head = head
        

    def insert(self,val):
        newNode = Node(val)
        if (self.head == None):
            self.head = newNode
            return
        curr = self.head
        while(curr.next != None):
            curr = curr.next
        curr.next = newNode

    def printList(self):
        curr = self.head

        while curr != None :
            print(curr.val , " -> ", end="")
            
            curr = curr.next
    def getHead(self):
        return self.head
    

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None   
        
h= Node(54)
List = LinkedList(h)

List.insert(0)
List.insert(54)
List.insert(85)
List.insert(85)

head = List.getHead()
printThroughHead(head)

            

