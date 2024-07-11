#reversing a string using stack
def createStack():
    stack = []
    return stack
def push(stack,data):
    stack.append(data)
def size(stack):
    return len(stack)
def isEmpty(stack):
    if len(stack)==0:
        return True
    else:
        return False
def pop(stack):
    if isEmpty(stack):
        return
    return stack.pop()
def reverse(string):
    n = len(string)
    stack = createStack()
    for i in range(n):
        push(stack, string[i])
    string = ''
    for i in range(n):
        string+= pop(stack)
    return string
str = "Saiyed K"
print(reverse(str))
    
