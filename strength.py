def getStrength(string):
    upper = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'
    lower = 'abcdefghijklmnopqrstuvxyz'
    nums = '1234567890'
    chars = '!@#$%^&*()_+{}:"<>,.?/*'
    i = 0
    if len(string) > 6:
        i+=1
    if len(string) > 10:
        i+=1
    for x in string:
        if x in upper:
            i+=1
            break
    for x in string:
        if x in lower:
            i+=1
            break
    for x in string:
        if x in nums:
            i+=1
            break
    for x in string:
        if x in chars:
            i+=1
            break
    return i
while True: 
    passw = input("Enter Password: ")
    s = getStrength(passw)
    if (s <= 2):
        print("Weak Password")
    if (s > 2) and (s <=4):
        print("Moderate Password")
    if (s > 4):
        print("Strong Password")

    
