f=open("saiyed.txt","w")
f.write("Hey, yo ")
f.close()
f=open("saiyed.txt","a")
f.write("apended stuff")
f.close()
f=open("saiyed.txt","r")
x=f.read()
print(x)