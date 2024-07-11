#binary tree
class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
    def insert(self,data):
        newNode = Node(data)
        if self.data:
            if data < self.data:
                if self.left == None:
                    self.left = newNode
                else:
                    self.left.insert(data)
            else:
                if self.right == None:
                    self.right = newNode
                else:
                    self.right.insert(data)
        else:
            self.data = data
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()
#Traversals
#PreOrder
def preOrder(root):
    print(root.data)
    if root.left:
        preOrder(root.left)
    if root.right:
        preOrder(root.right)
def inOrder(root):
    if root.left:
        inOrder(root.left)
    print(root.data)
    if root.right:
        inOrder(root.right)

def postOrder(root):
    if root.left:
        postOrder(root.left)
    if root.right:
        postOrder(root.right)
    print(root.data)

def search(root, data):
    if root.data == data:
        print("Found")
    elif data < root.data:
        if root.left:
            search(root.left, data)
        else:
            print("Not Found")
    else:
        if root.right:
            search(root.right, data)
        else:
            print("Not Found")
        
root = Node(44)
root.insert(55)
root.insert(33)
root.insert(22)
root.insert(89)
root.insert(21)
root.insert(66)
root.insert(8)
root.insert(74)
root.insert(99)
preOrder(root)
print("-----------------")
inOrder(root)
print("-----------------")
postOrder(root)
print("-----------------")
search(root,99)
