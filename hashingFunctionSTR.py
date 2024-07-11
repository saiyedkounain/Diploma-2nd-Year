#hashing functions
#for strings
def getHash(str):
    h = 0
    for i in range(len(str)):
        a = ord(str[i])
        h = h+a*i
    return h%26

print(getHash("Saiyed Kounain"))
print(getHash("Raseena Haneef"))
