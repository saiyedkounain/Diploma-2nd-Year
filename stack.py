# i change my mind gonna do a stack instead lol
# first in last out
stack=[]
def push():
    num = int(input("Enter stuff to add: "))
    stack.append(num)
    print (num, "is added to stack")
def pop():
    if not stack:
        print ("The stack is empty, you cannot delete stuff now")
    else:
        
        stack.pop()
        print("the last element is removed from stack")
        
def show():
    print(stack)



while True:
    print("Enter operation 1.Add 2.Remove 3.Show 4.Quit")
    oper = int(input())
    if oper==1:
        push()
    elif oper==2:
        pop()
    elif oper==3:
        show()
    elif oper == 4:
        break
    else:
        print("Enter a valid operation you peice of shit")
