#hashing functions
#for numbers
def getHash(data):
    key = data % 10
    return key
#driver code
n = 23
print("Hash Key: ", getHash(n))
